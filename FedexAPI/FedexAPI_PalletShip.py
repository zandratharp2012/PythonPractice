# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:00:04 2021

@author: ZTharp

This program will calculate cost for ground (boxes and envelopes only with 150lbs limit)



Fedex API Information:
Production Account Information 
Supported Web Services:	 	            FedEx Web Services for Shipping
Production URL: 			            https://ws.fedex.com:443/web-services 
(secrect id) Password: 			         
FedEx Shipping Account Number: 	         
FedEx Web Services Meter Number: 	     
(Client ID) Authentication Key:
LTL freight account number:

 


"""
import requests
import json
import sys
import logging
from fedex.config import FedexConfig
from fedex.services.rate_service import FedexRateServiceRequest
#from fedex.tools.conversion import sobject_to_dict
# Change these values to match your testing account/meter number.



def main():
 
    CONFIG_OBJ = FedexConfig(key='',
                           password='',
                           account_number='',
                           meter_number='',
                           freight_account_number= '',
                           use_test_server=False)
   
    rate = FedexRateServiceRequest(CONFIG_OBJ)
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    
    customer_transaction_id = "*** RateService Request v18 using Python ***"  # Optional transaction_id
    
    # This is the object that will be handling our request which is utilized to retrieve rates
    rate_request = FedexRateServiceRequest(CONFIG_OBJ, customer_transaction_id=customer_transaction_id)
    
    rate_request.RequestedShipment.ServiceType = 'FEDEX_FREIGHT_ECONOMY'

    rate_request.RequestedShipment.DropoffType = 'REGULAR_PICKUP'
    
    rate_request.RequestedShipment.PackagingType = 'YOUR_PACKAGING'
    
    rate_request.RequestedShipment.FreightShipmentDetail.TotalHandlingUnits = 1
    
    rate_request.RequestedShipment.FreightShipmentDetail.FedExFreightAccountNumber = CONFIG_OBJ.freight_account_number
    
    # Shipper
    rate_request.RequestedShipment.Shipper.AccountNumber = CONFIG_OBJ.freight_account_number
    rate_request.RequestedShipment.Shipper.Contact.PersonName = 'Sender Name'
    rate_request.RequestedShipment.Shipper.Contact.CompanyName = 'Customer ABC'
    rate_request.RequestedShipment.Shipper.Address.StreetLines = ['123 Parker Drive']
    rate_request.RequestedShipment.Shipper.Address.City = 'Austin'
    rate_request.RequestedShipment.Shipper.Address.StateOrProvinceCode = 'TX'
    rate_request.RequestedShipment.Shipper.Address.PostalCode = '78728'
    rate_request.RequestedShipment.Shipper.Address.CountryCode = 'US'
    rate_request.RequestedShipment.Shipper.Address.Residential = False
    
    # Recipient
    rate_request.RequestedShipment.Recipient.Address.City = 'Harrison'
    rate_request.RequestedShipment.Recipient.Address.StateOrProvinceCode = 'AR'
    rate_request.RequestedShipment.Recipient.Address.PostalCode = '72601'
    rate_request.RequestedShipment.Recipient.Address.CountryCode = 'US'
    rate_request.RequestedShipment.Shipper.Address.Residential = False
    
    # Payment
    payment = rate_request.create_wsdl_object_of_type('Payment')
    payment.PaymentType = "SENDER"
    payment.Payor.ResponsibleParty = rate_request.RequestedShipment.Shipper
    rate_request.RequestedShipment.ShippingChargesPayment = payment
    
    # include estimated duties and taxes in rate quote, can be ALL or NONE
    rate_request.RequestedShipment.EdtRequestType = 'NONE'
    
    # note: in order for this to work in test, you may need to use the
    # specially provided LTL addresses emailed to you when signing up.
    rate_request.RequestedShipment.FreightShipmentDetail.FedExFreightBillingContactAndAddress.Contact.PersonName = 'Sender Name'
    rate_request.RequestedShipment.FreightShipmentDetail.FedExFreightBillingContactAndAddress.Contact.CompanyName = 'Customer ABC'
    rate_request.RequestedShipment.FreightShipmentDetail.FedExFreightBillingContactAndAddress.Address.StreetLines = [
        '111 Circle Drive']
    rate_request.RequestedShipment.FreightShipmentDetail.FedExFreightBillingContactAndAddress.Address.City = 'Engelwood'
    rate_request.RequestedShipment.FreightShipmentDetail.FedExFreightBillingContactAndAddress.Address.StateOrProvinceCode = 'CO'
    rate_request.RequestedShipment.FreightShipmentDetail.FedExFreightBillingContactAndAddress.Address.PostalCode = '80111'
    rate_request.RequestedShipment.FreightShipmentDetail.FedExFreightBillingContactAndAddress.Address.CountryCode = 'US'
    rate_request.RequestedShipment.FreightShipmentDetail.FedExFreightBillingContactAndAddress.Address.Residential = False
    
    spec = rate_request.create_wsdl_object_of_type('ShippingDocumentSpecification')
    
    spec.ShippingDocumentTypes = [spec.CertificateOfOrigin]
    
    rate_request.RequestedShipment.ShippingDocumentSpecification = spec
    
    role = rate_request.create_wsdl_object_of_type('FreightShipmentRoleType')
    rate_request.RequestedShipment.FreightShipmentDetail.Role = role.SHIPPER
    
    # Designates the terms of the "collect" payment for a Freight
    # Shipment. Can be NON_RECOURSE_SHIPPER_SIGNED or STANDARD
    rate_request.RequestedShipment.FreightShipmentDetail.CollectTermsType = 'STANDARD'
    
    package1_weight = rate_request.create_wsdl_object_of_type('Weight')
    package1_weight.Value = 300.0
    package1_weight.Units = "LB"
    
    rate_request.RequestedShipment.FreightShipmentDetail.PalletWeight = package1_weight
    
    package1_dimensions = rate_request.create_wsdl_object_of_type('Dimensions')
    package1_dimensions.Length = 48
    package1_dimensions.Width = 40
    package1_dimensions.Height = 40
    package1_dimensions.Units = "IN"
    
    #rate_request.RequestedShipment.FreightShipmentDetail= package1_dimensions
    #print (package1_dimensions)    
    package1 = rate_request.create_wsdl_object_of_type('FreightShipmentLineItem')
    print(package1)    

    package1.Weight = package1_weight
    package1.Dimensions = package1_dimensions
    package1.Packaging = 'PALLET'
    package1.Description = 'Products'
    package1.FreightClass = 'CLASS_500'
 
    
    rate_request.RequestedShipment.FreightShipmentDetail.LineItems = package1
    print(package1)
    # If you'd like to see some documentation on the ship service WSDL, un-comment
    # this line. (Spammy).
    print(rate_request.client)
    
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
    
    # RateReplyDetails can contain rates for multiple ServiceTypes if ServiceType was set to None
    for service in rate_request.response.RateReplyDetails:
        for detail in service.RatedShipmentDetails:
            for surcharge in detail.ShipmentRateDetail.Surcharges:
                if surcharge.SurchargeType == 'OUT_OF_DELIVERY_AREA':
                    print("{}: ODA rate_request charge {}".format(service.ServiceType, surcharge.Amount.Amount))
    
        for rate_detail in service.RatedShipmentDetails:
            print("{}: Net FedEx Charge {} {}".format(service.ServiceType,
                                                      rate_detail.ShipmentRateDetail.TotalNetFedExCharge.Currency,
                                                      rate_detail.ShipmentRateDetail.TotalNetFedExCharge.Amount))

    
    
    
    
 
    # print('We called object that will contains all details for package1')
    # # # If you'd like to see some documentation on the ship service WSDL, un-comment
    # # # this line. (Spammy).
    # #print(rate_request.client)
    
   
    
    # #package1.GroupPackageCount = 1
    # # Un-comment this to see the other variables you may set on a package.
    # # print(package1)
    
    # # This adds the RequestedPackageLineItem WSDL object to the rate_request. It
    # # increments the package count and total weight of the rate_request for you.
    # #rate_request.add_package(package1)
    
    #  # # Un-comment this to see your complete, ready-to-send request as it stands
    # # # before it is actually sent. This is useful for seeing what values you can
    # # # change.
    # print(rate_request.RequestedShipment)
    # # # Fires off the request, sets the 'response' attribute on the object.
    # rate_request.send_request()
    
    # # # This will show the reply to your rate_request being sent. You can access the
    # # # attributes through the response attribute on the request object. This is
    # # # good to un-comment to see the variables returned by the FedEx reply.
    # # # print(rate_request.response)
    
    # # # This will convert the response to a python dict object. To
    # # # make it easier to work with.
    # # # from fedex.tools.conversion import basic_sobject_to_dict
    # # # print(basic_sobject_to_dict(rate_request.response))
    
    # # # This will dump the response data dict to json.
    # # # from fedex.tools.conversion import sobject_to_json
    # # # print(sobject_to_json(rate_request.response))
    
    # # # Here is the overall end result of the query.
    # # print("HighestSeverity: {}".format(rate_request.response.HighestSeverity))
    
    # # # RateReplyDetails can contain rates for multiple ServiceTypes if ServiceType was set to None
    # # for service in rate_request.response.RateReplyDetails:
    # #     for detail in service.RatedShipmentDetails:
    # #         for surcharge in detail.ShipmentRateDetail.Surcharges:
    # #             if surcharge.SurchargeType == 'OUT_OF_DELIVERY_AREA':
    # #                 print("{}: ODA rate_request charge {}".format(service.ServiceType, surcharge.Amount.Amount))
    
    # #     for rate_detail in service.RatedShipmentDetails:
    # #         print("{}: Net FedEx Charge {} {}".format(service.ServiceType,
    # #                                                   rate_detail.ShipmentRateDetail.TotalNetFedExCharge.Currency,
    # #                                                   rate_detail.ShipmentRateDetail.TotalNetFedExCharge.Amount))
                        
if __name__ == "__main__":
    main()    

















