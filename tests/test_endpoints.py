# Contracts
# 
# https://localhost:5000/v1/api/trsrv/secdef

# 
# https://localhost:5000/v1/api/trsrv/secdef/schedule

# Future Contract 
# https://localhost:5000/v1/api/trsrv/futures

# Contract Details
# https://localhost:5000/v1/api/iserver/contract/{conid}/info

# Market Data History
# https://localhost:5000/v1/api/hmds/history

# Scanner 
# https://localhost:5000/v1/api/hmds/scanner

# Run scanner to get a list of contracts 
# https://localhost:5000/v1/api/iserver/scanner/run

# Market data snapshot
#https://localhost:5000/v1/api/md/snapshot

# Market data cancel - single 
 # https://localhost:5000/v1/api/iserver/marketdata/{conid}/unsubscribe

# Market Data History 
# https://localhost:5000/v1/api/iserver/marketdata/history

# Portafolio Analyst
# https://localhost:5000/v1/api/pa/performance

# Account Balance's Summary
# https://localhost:5000/v1/api/pa/summary

# Position's Transaction History
# https://localhost:5000/v1/api/pa/transactions 

# Session - Authentication Status 
# https://localhost:5000/v1/api/iserver/auth/status

# Tries to re authenticate to brokerage 

# https://localhost:5000/v1/api/iserver/reauthenticate


# Ping the server to keep the session open
 # https://localhost:5000/v1/api/tickle 

 # Ends the current session 
 # https://localhost:5000/v1/api/logout

 # Account - portafolio accounts 
 # https://localhost:5000/v1/api/portfolio/accounts

 # List of Sub Accounts 
 #sed in tiered account structures (such as Financial Advisor and IBroker Accounts) to return a list of up to 
 # 100 sub-accounts for which the user can view position and account-related information. 
 # This endpoint must be called prior to calling other /portfolio endpoints for those sub-accounts.
 #  If you have more than 100 sub-accounts use /portfolio/subaccounts2. 
 # To query a list of accounts the user can trade, see /iserver/accounts.


 # https://localhost:5000/v1/api/portfolio/subaccounts

 # subaccounts 
 # https://localhost:5000/v1/api/portfolio/subaccounts2

 # Account Information
 # https://localhost:5000/v1/api/portfolio/{accountId}/meta

 # Account Summary 
 # https://localhost:5000/v1/api/portfolio/{accountId}/summary

 

