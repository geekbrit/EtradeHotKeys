import os

sandboxMode = True


if sandboxMode:
    client_Consumer_Key    = os.environ['ETRADE_SANDBOX_KEY']
    client_Consumer_Secret = os.environ['ETRADE_SANDBOX_SECRET']
else:
    client_Consumer_Key    = os.environ['ETRADE_PRODUCTION_KEY']
    client_Consumer_Secret = os.environ['ETRADE_PRODUCTION_SECRET']

