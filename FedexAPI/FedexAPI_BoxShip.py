# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:00:04 2021

@author: ZTharp

C# Library using Shippo:
    https://github.com/goshippo/shippo-csharp-client 
 
C# Library using Fedex Examples and payload request:
    https://developer.fedex.com/api/en-us/catalog/rate/v1/docs.html
    
https://developer.fedex.com/api/en-us/catalog/authorization/v1/docs.html - Authentication
https://developer.fedex.com/api/en-us/catalog/rate/v1/docs.html - Rates

This program will calculate cost for ground (boxes only with 150lbs limit)

Production Account Information (Fedex APIs)
Supported Web Services:	 	             FedEx Web Services for Shipping
Production URL: 			             https://ws.fedex.com:443/web-services 
(secrect id) Password: 			         
FedEx Shipping Account Number: 	         
FedEx Web Services Meter Number: 	      
(Client ID) Authentication Key:	 	       
Fedex Freight Account Number:
"""
import requests
import json
import sys
import os
import logging
import pandas as pd
from fedex.config import FedexConfig
from fedex.services.track_service import FedexTrackRequest
from fedex.services.rate_service import FedexRateServiceRequest
#from fedex.tools.conversion import sobject_to_dict
#Change these values to match your testing account/meter number.



def main():
 
    CONFIG_OBJ = FedexConfig(key='',
                           password='V',
                           account_number='',
                           meter_number='',
                           use_test_server=False)
    rate = FedexRateServiceRequest(CONFIG_OBJ)
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    
 
    customer_transaction_id = "*** RateService Request v18 using Python ***"  # Optional transaction_id
    
    # This is the object that will be handling our request which is utilized to retrieve rates
    rate_request = FedexRateServiceRequest(CONFIG_OBJ, customer_transaction_id=customer_transaction_id)
    #print(rate_request)
    
    # If you wish to have transit data returned with your request you
    # need to uncomment the following
    # rate_request.ReturnTransitAndCommit = True
    
    # This is very generalized, top-level information.
    # REGULAR_PICKUP, REQUEST_COURIER, DROP_BOX, BUSINESS_SERVICE_CENTER or STATION
    rate_request.RequestedShipment.DropoffType = 'BUSINESS_SERVICE_CENTER'
    
    # See page 355 in WS_ShipService.pdf for a full list. Here are the common ones:
    # STANDARD_OVERNIGHT, PRIORITY_OVERNIGHT, FEDEX_GROUND, FEDEX_EXPRESS_SAVER
    # To receive rates for multiple ServiceTypes set to None.
    rate_request.RequestedShipment.ServiceType = 'PRIORITY_OVERNIGHT'
    
    # What kind of package this will be shipped in.
    # FEDEX_BOX, FEDEX_PAK, FEDEX_TUBE, YOUR_PACKAGING
    rate_request.RequestedShipment.PackagingType = 'YOUR_PACKAGING'
    
    # Shipper's address
    rate_request.RequestedShipment.Shipper.Address.StateOrProvinceCode = 'TX'
    rate_request.RequestedShipment.Shipper.Address.PostalCode = '78728'
    rate_request.RequestedShipment.Shipper.Address.CountryCode = 'US'
    rate_request.RequestedShipment.Shipper.Address.Residential = False
    
    # Recipient address
    rate_request.RequestedShipment.Recipient.Address.StateOrProvinceCode = 'NC'
    rate_request.RequestedShipment.Recipient.Address.PostalCode = '27577'
    rate_request.RequestedShipment.Recipient.Address.CountryCode = 'US'
    # This is needed to ensure an accurate rate quote with the response.
    # rate_request.RequestedShipment.Recipient.Address.Residential = True
    # include estimated duties and taxes in rate quote, can be ALL or NONE
    rate_request.RequestedShipment.EdtRequestType = 'NONE'
    
    # Who pays for the rate_request?
    # RECIPIENT, SENDER or THIRD_PARTY
    rate_request.RequestedShipment.ShippingChargesPayment.PaymentType = 'SENDER'
    
    # See https://www.fedex.com/us/developer/downloads/pdfs/2021/FedEx_WebServices_RateServices_WSDLGuide_v2021.pdf  for a full list. 
    #Here are the common ones:
    # Weight, Dimensions
    
    package1_weight = rate_request.create_wsdl_object_of_type('Weight')
    # Weight, in LB. and limit is 150lbs for box shipments
    package1_weight.Value = 300
    package1_weight.Units = "LB"
    
    package1_dimensions = rate_request.create_wsdl_object_of_type('Dimensions')
    # Dimensions, in IN
    # Box size choices: 22X15X15, 24X18X18, 12X10X6, 18X12X12, 14X14X6
    package1_dimensions.Length = 48
    package1_dimensions.Width = 40
    package1_dimensions.Height = 55
    package1_dimensions.Units = "IN"
    
    package1 = rate_request.create_wsdl_object_of_type('RequestedPackageLineItem')
    package1.Weight = package1_weight
    package1.Dimensions = package1_dimensions
    # can be other values this is probably the most common
    package1.PhysicalPackaging = 'BOX'
    # Required, but according to FedEx docs:
    # "Used only with PACKAGE_GROUPS, as a count of packages within a
    # group of identical packages". In practice you can use this to get rates
    # for a shipment with multiple packages of an identical package size/weight
    # on rate request without creating multiple RequestedPackageLineItem elements.
    # You can OPTIONALLY specify a package group:
    # package1.GroupNumber = 0  # default is 0
    # The result will be found in RatedPackageDetail, with specified GroupNumber.
    package1.GroupPackageCount = 1
   
    # Un-comment this to see the other variables you may set on a package.
    # print(package1)
    
    # This adds the RequestedPackageLineItem WSDL object to the rate_request. It
    # increments the package count and total weight of the rate_request for you.
    rate_request.add_package(package1)
    
    # If you'd like to see some documentation on the ship service WSDL, un-comment
    # this line. (Spammy).
    # print(rate_request.client)
    
    # Un-comment this to see your complete, ready-to-send request as it stands
    # before it is actually sent. This is useful for seeing what values you can
    # change.
    # print(rate_request.RequestedShipment)
    
    # Fires off the request, sets the 'response' attribute on the object.
    rate_request.send_request()
    
    # This will show the reply to your rate_request being sent. You can access the
    # attributes through the response attribute on the request object. This is
    # good to un-comment to see the variables returned by the FedEx reply.
    # print(rate_request.response)
    
    # This will convert the response to a python dict object. To
    # make it easier to work with.
    # from fedex.tools.conversion import basic_sobject_to_dict
    # print(basic_sobject_to_dict(rate_request.response))
    
    # This will dump the response data dict to json.
    # from fedex.tools.conversion import sobject_to_json
    # print(sobject_to_json(rate_request.response))
    
    # Here is the overall end result of the query.
    print("HighestSeverity: {}".format(rate_request.response.HighestSeverity))
    
    df = pd.DataFrame()
    df2=pd.DataFrame()
    counter = 0 
    
    # RateReplyDetails can contain rates for multiple ServiceTypes if ServiceType was set to None
    for service in rate_request.response.RateReplyDetails:
        for detail in service.RatedShipmentDetails:
            for surcharge in detail.ShipmentRateDetail.Surcharges:
                if surcharge.SurchargeType == 'OUT_OF_DELIVERY_AREA':
                    print("{}: ODA rate_request charge {}".format(service.ServiceType, surcharge.Amount.Amount))
        
        #print fedex charge details (cost)
        for rate_detail in service.RatedShipmentDetails:
            #rate_detail=("{}: Net FedEx Charge {} {}".format(service.ServiceType,
             #                                          rate_detail.ShipmentRateDetail.TotalNetFedExCharge.Currency,
               #                                       rate_detail.ShipmentRateDetail.TotalNetFedExCharge.Amount))
            rate_detail=rate_detail.ShipmentRateDetail.TotalNetFedExCharge.Amount
            if counter==0:
                your_rate=float(rate_detail)
                print('\nYour rate \n', your_rate)
                df = df.append({'Your_rate': your_rate}, ignore_index=True)

            else: 
                more_rates = float(rate_detail)
                print('\nMultiweight Rate \n',more_rates)
                df['Multiweight_rate'] = more_rates           
            
            counter=+1
            
            
            
            my_dir = ''
            file_name = 'Fedex_Box_Quote.csv'
            fname = os.path.join(my_dir, file_name)
            df.to_csv(fname,index=False )
            
            
        # Check for warnings, this is also logged by the base class.
        # if rate_request.response.HighestSeverity == 'NOTE':
        #     for notification in rate_request.response.Notifications:
        #         if notification.Severity == 'NOTE':
        #             print(sobject_to_dict(notification))



if __name__ == "__main__":
    main()    

















