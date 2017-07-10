import os

# GLOBAL CONFIG SETTINGS
#sandboxMode = True

#-----------------------------------------------------------------------------
#  STOPLOSS is used to place an emergency get-out order in case the
#  stock quickly reverses & goes bad.
#
#  Set to zero to prevent the stop order from being placed automatically
#  Experimenting with percent vs dollars.
#  200 dollar stop loss gave some expensive early bailouts on very big orders
#-----------------------------------------------------------------------------

TRADESIZE   = 7000 #dollars
STOPLOSS    =  140 #dollars
STOPTYPE    = 'DOLLARS' #'DOLLARS'or 'PERCENT'

try:
    sandboxMode
    client_Consumer_Key    = os.environ['ETRADE_SANDBOX_KEY']
    client_Consumer_Secret = os.environ['ETRADE_SANDBOX_SECRET']
except NameError:
    client_Consumer_Key    = os.environ['ETRADE_PRODUCTION_KEY']
    client_Consumer_Secret = os.environ['ETRADE_PRODUCTION_SECRET']
    sandboxMode = False

