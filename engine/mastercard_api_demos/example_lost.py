from mastercardapicore import RequestMap, Config, OAuthAuthentication
from os.path import dirname, realpath, join
from os import getenv
from mastercardloststolen import AccountInquiry

def main(params={}):
    if not params:
        account_number = "5222222222222200"
    else:
        account_number = params.get("account_number")

    consumerKey = getenv("CONSUMER_KEY")
    keyStorePath = getenv("KEY_STORE_PATH") # e.g. /Users/yourname/project/sandbox.p12 | C:\Users\yourname\project\sandbox.p12
    keyAlias = "keyalias"   # For production: change this to the key alias you chose when you created your production key
    keyPassword = "keystorepassword"   # For production: change this to the key alias you chose when you created your production key

    auth = OAuthAuthentication(consumerKey, keyStorePath, keyAlias, keyPassword)
    Config.setAuthentication(auth)
    Config.setSandbox(True)   # For production: use Config.setSandbox(false)

    mapObj = RequestMap()
    mapObj.set("AccountInquiry.AccountNumber", account_number)

    try:
        request = AccountInquiry(mapObj)
        response = request.update()
        print("Account.Listed--> %s") % response.get("Account.Listed") #Account.Listed-->True
        print("Account.ReasonCode--> %s") % response.get("Account.ReasonCode") #Account.ReasonCode-->L
        print("Account.Reason--> %s") % response.get("Account.Reason") #Account.Reason-->LOST
    except Exception:
        raise

    return response.__dict__
    

if __name__ == "__main__":
    resp = main()
    print(resp)
