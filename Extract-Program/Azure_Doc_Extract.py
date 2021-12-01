# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:17:59 2021

@author: ZTharp
"""
import pandas as pd
from azure.storage.blob import BlobServiceClient,BlobProperties,BlobClient,ContainerClient
from io import BytesIO
from sqlalchemy import create_engine
from six.moves import urllib
import os
import io
import xlrd as xl
import openpyxl


local_path = "" #Set desired local path
conn_string = "DefaultEndpointsProtocol=;AccountName=;AccountKey=pw==;EndpointSuffix=" #Update with your current storage credentials
container_name = "" #Set starting container
processed_container = "" #Set ending storage container
blob_service_client = BlobServiceClient.from_connection_string(conn_str= conn_string)# Connect to Blob 
container_client = blob_service_client.get_container_client(container_name)
blob_list = container_client.list_blobs()
bloblist = []

def main():
    
    #Prior to script, this is where power automation would take place to extract file from sharepoint location and place in azure storage location
    print("Fetching destination in blob container")
    for blob in container_client.list_blobs():
        bloblist.append(blob.name)
     
        
    print('You have succesfully connected to Azure and printed your blob list which is listed below: /n')
    print(bloblist)
    
    
    df_final=pd.DataFrame()
    
    #Set columns for staging dataframe and finalized dataframe as well as part numbers that meet requirements
    names = ['Project Number','Date Quoted','Customer','End User','Services Summary','Delivery Group',
             'Part Number','Margin (%)','Cost per Hop','Total Cost',
             'Sell per Hop',	'Total Sell', 'NA','Hops', 'Sites']


    part_no = ['SVCS-IN-IC-AS','SVCS-IN-IC-FI','SVCS-IN-IC-FI-DCD','SVCS-IN-IC-FI-SU','SVCS-IN-IC-FI-TC','SVCS-IN-SS-WH']
    
    for key in dict.fromkeys(bloblist):
        if key.endswith('.xlsx') or key.endswith('.xlsm'): 
            #if file name ends with these extensions, then follow through with the program
            #otherwise throw exception and pass on to the next file
            try:
                blob_client = blob_service_client.get_blob_client(container=container_name, blob=key)#download Blob
                df=pd.DataFrame()
                df=(blob_client.download_blob().readall())
              
                work_book = pd.ExcelFile(df)#define workbook
                worksheetnames= work_book.sheet_names
                print("Sheets in workbook: ", worksheetnames)
                print("Loading summary Tab..")
                df=pd.read_excel(work_book, sheet_name='Summary', header=None)
                df.insert(0, 'Project Number',"",True)
                df.insert(1, 'Customer',"",True)
                df.insert(2, 'End User',"",True)
                df.insert(1, 'Date Quoted:',"", True)
                
                
                df=df.iloc[:,:15]
               
                #Add headers for the first dataframe coming from summary tab of field services quote
                df.columns=names
                
                #Find MSO
                df_MSO=df[df['Services Summary'].str.contains("MSO #", na=False)]
                MSO=df_MSO.at[2,'Delivery Group']
                #Assign MSO to all rows 
                df['Project Number'] = MSO
                
                #Find Customer
                df_cx=df[df['Services Summary'].str.contains("Customer:", na=False)]
                cx=df_cx.at[0,'Delivery Group']
                #Assign Customer Name to all rows 
                df['Customer'] = cx
               
                #Find End customer
                df_end_cx=df[df['Services Summary'].str.contains("End User/Project Description:", na=False)]
                end_cx=df_end_cx.at[1,'Delivery Group']
                #Assign End User and Project Description to all rows
                df['End User'] = end_cx
                
              
                #Find Date Quoted
                df_Date=df[df['Services Summary'].str.contains("Date Quoted:", na=False)] 
                date_Quoted=df_Date.at[3,'Delivery Group'] #Extract the date
                #Assign date quoted to all rows
                df['Date Quoted']=date_Quoted 
                
              
                #Find No of Hops
                df_Hops=df[df['Services Summary'].str.contains("End User/Project Description:", na=False)]
                Hops=df_Hops.at[1,'Hops'] #Assign int hops to a variable
                df['Hops']=Hops #Assign int number of hops to all rows
                
                # Find No of Sites
                df_Sites=df[df['Services Summary'].str.contains("End User/Project Description:", na=False)]          
                Sites=df_Sites.at[1,'Sites'] #Assign int hops to a variable
                df['Sites']=Sites #Assign int number of hops to all rows
                
                
                #Drop all rows that do not have service summary lines and that do not contain part numbers in list
                df_staging=df.dropna(subset=['Services Summary']) 
                df_staging = df_staging.loc[df['Part Number'].isin(part_no)]
                #df = df_staging.loc[df['Cost per Hop'] != 0]
                
                print("""Pushed changes into df_staging dataframe. Now fetching state...
                      
                      **************************************************************
                     
                      """)
                #Find State in services quote sheet      
                df2 = pd.read_excel(work_book, sheet_name='SERVICES QUOTE',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],header=None)
                df2=df2.head(150)    

                df2.columns=['Col A','Col B','Col C','Col D','Col E','Col F', 'Col G', 'Col H', 'Col I', 'Col J', 'Col K', 'Col L',
                              'Col M', 'Col N', 'Col O', 'Col P', 'Col Q', 'Col R', 'Col S']
                
                # path = askdirectory(title='Select Folder') # shows dialog box and return the path
                # print("Path: " + path)
                # final_filename = 'SERVICESQUOTE SHEET.xlsx'
                # final_path = os.path.join(path,final_filename) 
                # #export df to csv in the indicated directory 
                # df2.to_excel(final_path,index=None)
                
                get_state = df2.iat[17,5] 
                print(get_state)
                
                get_prevailing = df2.iat[29,18].astype(int)
                print(get_prevailing)
                #insert state into the staging dataframe
                df_staging.insert(2, 'State', get_state, True) #Insert a new column with the date extracted in temp df for all rows
                df_staging.insert(14, 'Prevailing Wages', get_prevailing, True) #Insert a new column with the date extracted in temp df for all rows
                #append lines to a final df that will contain all database information
                df_final=df_final.append(df_staging)
    
                
            except TypeError: #If file is not part of criteria, pass in loop
                   pass 
        else:
            #print an error message and move to next item in for loop 
            print("This type of file is not supported: \n" + key)
            print("\n")
            pass 
        
   
    #Get the path of the final dataframe
    service_client_final = BlobServiceClient.from_connection_string(conn_string)
    client_final = service_client_final.get_container_client(processed_container)
    #Upload the file to blob container
    output = df_final.to_csv(encoding='utf-8')
    # output=df_final.to_excel
    
    # writer=io.BytesIO()
    # output=df_final.to_excel(writer)
    
    blob_block = ContainerClient.from_connection_string(conn_str=conn_string,container_name='')
    blob_block.upload_blob('Services_Database.csv', output, overwrite=True, encoding='utf-8')
    
    print('Program completed and now uploading database file')
    
if __name__ == "__main__":
    main()
