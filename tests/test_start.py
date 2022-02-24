
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
account_data = ib_client.portfolio_accounts()

# print the data.
print(account_data)

# Grab historical prices.
aapl_prices = ib_client.market_data_history(conid=['265598'], period='1d', bar='5min')

# print the prices.

print(aapl_prices)


# MARKET BUY ORDER, ENTER A POSITION.

tesla_order = ib_client.market_data_history(conid=['76792991'], side='BUY', quantity='1', period='1d', bar='5min')


print('tesla_order')

# close the current session.
ib_client.close_session()