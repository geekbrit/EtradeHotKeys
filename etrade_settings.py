import os

# GLOBAL CONFIG SETTINGS
sandboxMode = False
#sandboxMode = True

TRADESIZE = 7000 #dollars

if not sandboxMode:
    client_Consumer_Key    = os.environ['ETRADE_PRODUCTION_KEY']
    client_Consumer_Secret = os.environ['ETRADE_PRODUCTION_SECRET']
else:
    client_Consumer_Key    = os.environ['ETRADE_SANDBOX_KEY']
    client_Consumer_Secret = os.environ['ETRADE_SANDBOX_SECRET']

