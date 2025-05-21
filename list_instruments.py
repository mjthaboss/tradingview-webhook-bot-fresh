import oandapyV20
import oandapyV20.endpoints.accounts as accounts
from config import OANDA_API_KEY, OANDA_ACCOUNT_ID

client = oandapyV20.API(access_token=OANDA_API_KEY)

def list_instruments(account_id):
    r = accounts.AccountInstruments(accountID=account_id)
    response = client.request(r)
    instruments_list = response.get("instruments", [])
    for instr in instruments_list:
        print(instr["name"])

list_instruments(OANDA_ACCOUNT_ID)
