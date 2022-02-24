
from ibw.client import IBClient

REGULAR_ACCOUNT = 'DU5001780'
REGULAR_USERNAME = 'btrad5149'

# Create a new session of the IB Web API.
ib_client = IBClient(
    username=REGULAR_USERNAME,
    account=REGULAR_ACCOUNT,
    is_server_running=True
)


# create a new session.

ib_client.create_session()

# grab the account data.

account_Data = ib_client.portafolio_accounts()

# print the data.

print(account_Data)

# Grab historical prices

#appl_prices = ib_client.market_data_history(
 #   conid=['265598'], period='2h', bar='1min')
#print(appl_prices)
#print('')

# Grab current quotes

quote_fields = [55, 7296, 7295, 86, 70, 71, 84, 31]
appl_current_prices = ib_client.market_data(
conids=['265598'], since='0', fields=quote_fields)
print(appl_current_prices)
print('')


# close the current session.
ib_client.close_session()