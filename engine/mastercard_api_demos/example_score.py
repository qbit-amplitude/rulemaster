from mastercardapicore import RequestMap, Config, OAuthAuthentication
from os.path import dirname, realpath, join
from os import getenv
from mastercardfraudscoring import ScoreLookup


def main(params={}):
    if not params:
        customer_identifier = "1996"
        merchant_identifier = "12345"
        account_number = "5555555555555555"
        account_prefix = "555555"
        account_suffix = "5555"
        transaction_amount = "12500"
        transaction_date = "1231"
        transaction_time = "035931"
        bank_net_reference_number = "abc123hij"
        stan = "123456"
    else:
        customer_identifier = params.get("customer_identifier")
        merchant_identifier = params.get("merchant_identifier")
        account_number = params.get("account_number")
        account_prefix = params.get("account_prefix")
        account_suffix = params.get("account_suffix")
        transaction_amount = params.get("transaction_amount")
        transaction_date = params.get("transaction_date")
        transaction_time = params.get("transaction_time")
        bank_net_reference_number = params.get("bank_net_reference_number")
        stan = params.get("stan")

    consumerKey = getenv("CONSUMER_KEY")
    keyStorePath = getenv("KEY_STORE_PATH") # e.g. /Users/yourname/project/sandbox.p12 | C:\Users\yourname\project\sandbox.p12
    keyAlias = "keyalias"   # For production: change this to the key alias you chose when you created your production key
    keyPassword = "keystorepassword"   # For production: change this to the key alias you chose when you created your production key

    auth = OAuthAuthentication(consumerKey, keyStorePath, keyAlias, keyPassword)
    Config.setAuthentication(auth)
    Config.setSandbox(True)   # For production: use Config.setSandbox(false)

    mapObj = RequestMap()
    mapObj.set("ScoreLookupRequest.TransactionDetail.CustomerIdentifier", customer_identifier)
    mapObj.set("ScoreLookupRequest.TransactionDetail.MerchantIdentifier", merchant_identifier)
    mapObj.set("ScoreLookupRequest.TransactionDetail.AccountNumber", account_number)
    mapObj.set("ScoreLookupRequest.TransactionDetail.AccountPrefix", account_prefix)
    mapObj.set("ScoreLookupRequest.TransactionDetail.AccountSuffix", account_suffix)
    mapObj.set("ScoreLookupRequest.TransactionDetail.TransactionAmount", transaction_amount)
    mapObj.set("ScoreLookupRequest.TransactionDetail.TransactionDate", transaction_date)
    mapObj.set("ScoreLookupRequest.TransactionDetail.TransactionTime", transaction_time)
    mapObj.set("ScoreLookupRequest.TransactionDetail.BankNetReferenceNumber", bank_net_reference_number)
    mapObj.set("ScoreLookupRequest.TransactionDetail.Stan", stan)

    try:
        request = ScoreLookup(mapObj)
        response = request.update()
        print("ScoreLookup.CustomerIdentifier--> %s") % response.get("ScoreLookup.CustomerIdentifier") #ScoreLookup.CustomerIdentifier-->L5BsiPgaF-O3qA36znUATgQXwJB6MRoMSdhjd7wt50c97279
        print("ScoreLookup.TransactionDetail.CustomerIdentifier--> %s") % response.get("ScoreLookup.TransactionDetail.CustomerIdentifier") #ScoreLookup.TransactionDetail.CustomerIdentifier-->1996
        print("ScoreLookup.TransactionDetail.MerchantIdentifier--> %s") % response.get("ScoreLookup.TransactionDetail.MerchantIdentifier") #ScoreLookup.TransactionDetail.MerchantIdentifier-->12345
        print("ScoreLookup.TransactionDetail.AccountNumber--> %s") % response.get("ScoreLookup.TransactionDetail.AccountNumber") #ScoreLookup.TransactionDetail.AccountNumber-->5555555555555555
        print("ScoreLookup.TransactionDetail.AccountPrefix--> %s") % response.get("ScoreLookup.TransactionDetail.AccountPrefix") #ScoreLookup.TransactionDetail.AccountPrefix-->555555
        print("ScoreLookup.TransactionDetail.AccountSuffix--> %s") % response.get("ScoreLookup.TransactionDetail.AccountSuffix") #ScoreLookup.TransactionDetail.AccountSuffix-->5555
        print("ScoreLookup.TransactionDetail.TransactionAmount--> %s") % response.get("ScoreLookup.TransactionDetail.TransactionAmount") #ScoreLookup.TransactionDetail.TransactionAmount-->12500
        print("ScoreLookup.TransactionDetail.TransactionDate--> %s") % response.get("ScoreLookup.TransactionDetail.TransactionDate") #ScoreLookup.TransactionDetail.TransactionDate-->1231
        print("ScoreLookup.TransactionDetail.TransactionTime--> %s") % response.get("ScoreLookup.TransactionDetail.TransactionTime") #ScoreLookup.TransactionDetail.TransactionTime-->035931
        print("ScoreLookup.TransactionDetail.BankNetReferenceNumber--> %s") % response.get("ScoreLookup.TransactionDetail.BankNetReferenceNumber") #ScoreLookup.TransactionDetail.BankNetReferenceNumber-->abc123hij
        print("ScoreLookup.TransactionDetail.Stan--> %s") % response.get("ScoreLookup.TransactionDetail.Stan") #ScoreLookup.TransactionDetail.Stan-->123456
        print("ScoreLookup.ScoreResponse.MatchIndicator--> %s") % response.get("ScoreLookup.ScoreResponse.MatchIndicator") #ScoreLookup.ScoreResponse.MatchIndicator-->2
        print("ScoreLookup.ScoreResponse.FraudScore--> %s") % response.get("ScoreLookup.ScoreResponse.FraudScore") #ScoreLookup.ScoreResponse.FraudScore-->681
        print("ScoreLookup.ScoreResponse.ReasonCode--> %s") % response.get("ScoreLookup.ScoreResponse.ReasonCode") #ScoreLookup.ScoreResponse.ReasonCode-->A5
        print("ScoreLookup.ScoreResponse.RulesAdjustedScore--> %s") % response.get("ScoreLookup.ScoreResponse.RulesAdjustedScore") #ScoreLookup.ScoreResponse.RulesAdjustedScore-->701
        print("ScoreLookup.ScoreResponse.RulesAdjustedReasonCode--> %s") % response.get("ScoreLookup.ScoreResponse.RulesAdjustedReasonCode") #ScoreLookup.ScoreResponse.RulesAdjustedReasonCode-->19
        print("ScoreLookup.ScoreResponse.RulesAdjustedReasonCodeSecondary--> %s") % response.get("ScoreLookup.ScoreResponse.RulesAdjustedReasonCodeSecondary") #ScoreLookup.ScoreResponse.RulesAdjustedReasonCodeSecondary-->A9
    except Exception:
        raise

    return response.__dict__


if __name__ == "__main__":
    resp = main()
    print(resp)
