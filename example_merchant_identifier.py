#
#
# Script-Name: example_merchant_identifier
#

from mastercardapicore import RequestMap, Config, APIException, OAuthAuthentication
from os.path import dirname, realpath, join
from os import getenv
from mastercardmerchantidentifier import MerchantIdentifier

def main():
    consumerKey = getenv("CONSUMER_KEY")
    keyStorePath = getenv("KEY_STORE_PATH") # e.g. /Users/yourname/project/sandbox.p12 | C:\Users\yourname\project\sandbox.p12
    keyAlias = "keyalias"  # For production: change this to the key alias you chose when you created your production key
    keyPassword = "keystorepassword"  # For production: change this to the key alias you chose when you created your production key
    
    auth = OAuthAuthentication(consumerKey, keyStorePath, keyAlias, keyPassword)
    Config.setAuthentication(auth)
    Config.setDebug(True) # Enable http wire logging
    Config.setSandbox(True)
    
    try:
    	mapObj = RequestMap()
    	mapObj.set("MerchantId", "HOLIDAYINNEXPRESSWATERTOWNWI")
    	mapObj.set("Type", "FuzzyMatch")
    	response = MerchantIdentifier.query(mapObj)
    	print("MerchantIds.Message--> %s") % response.get("MerchantIds.Message") #MerchantIds.Message-->1 merchants found.
    	print("MerchantIds.ReturnedMerchants.Merchant[0].Address.Line1--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].Address.Line1") #MerchantIds.ReturnedMerchants.Merchant[0].Address.Line1-->101 AVIATION WAY
    	print("MerchantIds.ReturnedMerchants.Merchant[0].Address.Line2--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].Address.Line2") #MerchantIds.ReturnedMerchants.Merchant[0].Address.Line2-->
    	print("MerchantIds.ReturnedMerchants.Merchant[0].Address.City--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].Address.City") #MerchantIds.ReturnedMerchants.Merchant[0].Address.City-->WATERTOWN
    	print("MerchantIds.ReturnedMerchants.Merchant[0].Address.PostalCode--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].Address.PostalCode") #MerchantIds.ReturnedMerchants.Merchant[0].Address.PostalCode-->53094
    	print("MerchantIds.ReturnedMerchants.Merchant[0].Address.CountrySubdivision.Name--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].Address.CountrySubdivision.Name") #MerchantIds.ReturnedMerchants.Merchant[0].Address.CountrySubdivision.Name-->
    	print("MerchantIds.ReturnedMerchants.Merchant[0].Address.CountrySubdivision.Code--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].Address.CountrySubdivision.Code") #MerchantIds.ReturnedMerchants.Merchant[0].Address.CountrySubdivision.Code-->WI
    	print("MerchantIds.ReturnedMerchants.Merchant[0].Address.Country.Name--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].Address.Country.Name") #MerchantIds.ReturnedMerchants.Merchant[0].Address.Country.Name-->UNITED STATES
    	print("MerchantIds.ReturnedMerchants.Merchant[0].Address.Country.Code--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].Address.Country.Code") #MerchantIds.ReturnedMerchants.Merchant[0].Address.Country.Code-->USA
    	print("MerchantIds.ReturnedMerchants.Merchant[0].PhoneNumber--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].PhoneNumber") #MerchantIds.ReturnedMerchants.Merchant[0].PhoneNumber-->9202621910
    	print("MerchantIds.ReturnedMerchants.Merchant[0].BrandName--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].BrandName") #MerchantIds.ReturnedMerchants.Merchant[0].BrandName-->
    	print("MerchantIds.ReturnedMerchants.Merchant[0].MerchantCategory--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].MerchantCategory") #MerchantIds.ReturnedMerchants.Merchant[0].MerchantCategory-->3501 - HOLIDAY INNS
    	print("MerchantIds.ReturnedMerchants.Merchant[0].MerchantDbaName--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].MerchantDbaName") #MerchantIds.ReturnedMerchants.Merchant[0].MerchantDbaName-->HOLIDAY INN EXPRESS
    	print("MerchantIds.ReturnedMerchants.Merchant[0].DescriptorText--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].DescriptorText") #MerchantIds.ReturnedMerchants.Merchant[0].DescriptorText-->HOLIDAYINNEXPRESSWATERTOWNWI
    	print("MerchantIds.ReturnedMerchants.Merchant[0].LegalCorporateName--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].LegalCorporateName") #MerchantIds.ReturnedMerchants.Merchant[0].LegalCorporateName-->
    	print("MerchantIds.ReturnedMerchants.Merchant[0].Comment--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].Comment") #MerchantIds.ReturnedMerchants.Merchant[0].Comment-->
    	print("MerchantIds.ReturnedMerchants.Merchant[0].LocationId--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].LocationId") #MerchantIds.ReturnedMerchants.Merchant[0].LocationId-->49751863
    	print("MerchantIds.ReturnedMerchants.Merchant[0].SoleProprietorName--> %s") % response.get("MerchantIds.ReturnedMerchants.Merchant[0].SoleProprietorName") #MerchantIds.ReturnedMerchants.Merchant[0].SoleProprietorName-->
    
    except APIException as e:
    	print("HttpStatus: %s") % e.getHttpStatus()
    	print("Message: %s") % e.getMessage()
    	print("ReasonCode: %s") % e.getReasonCode()
    	print("Source: %s") % e.getSource()

if __name__ == "__main__": main()
