#!/usr/bin/env python
import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
from PyQt4 import QtGui
from PyQt4.QtCore import QTimer
import sys
import hkeys
import etradepy

class EtradeApp(QtGui.QMainWindow, hkeys.Ui_MainWindow):
    def __init__(self, parent=None):
        super(EtradeApp, self).__init__(parent)
        self.setupUi(self)

        self.cleartimer = QTimer()
        self.cleartimer.timeout.connect(lambda : self.statusBar.showMessage( "" ) )

        #
        self.Buy_1.clicked.connect(lambda : self.buy(self.T_1, self.qty_1))
        self.Buy_2.clicked.connect(lambda : self.buy(self.T_2, self.qty_2))
        self.Buy_3.clicked.connect(lambda : self.buy(self.T_3, self.qty_3))
        self.Buy_4.clicked.connect(lambda : self.buy(self.T_4, self.qty_4))
        self.Buy_5.clicked.connect(lambda : self.buy(self.T_5, self.qty_5))
        #
        self.Sell_1.clicked.connect(lambda : self.sell(self.T_1, self.qty_1))
        self.Sell_2.clicked.connect(lambda : self.sell(self.T_2, self.qty_2))
        self.Sell_3.clicked.connect(lambda : self.sell(self.T_3, self.qty_3))
        self.Sell_4.clicked.connect(lambda : self.sell(self.T_4, self.qty_4))
        self.Sell_5.clicked.connect(lambda : self.sell(self.T_5, self.qty_5))
        #
        self.SLimit_1.clicked.connect(lambda : self.slimit(self.T_1, self.qty_1, self.price_1))
        self.SLimit_2.clicked.connect(lambda : self.slimit(self.T_2, self.qty_2, self.price_2))
        self.SLimit_3.clicked.connect(lambda : self.slimit(self.T_3, self.qty_3, self.price_3))
        self.SLimit_4.clicked.connect(lambda : self.slimit(self.T_4, self.qty_4, self.price_4))
        self.SLimit_5.clicked.connect(lambda : self.slimit(self.T_5, self.qty_5, self.price_5))
        #
        self.SLoss_1.clicked.connect(lambda : self.stoploss(self.T_1, self.qty_1, self.loss_1))
        self.SLoss_2.clicked.connect(lambda : self.stoploss(self.T_2, self.qty_2, self.loss_2))
        self.SLoss_3.clicked.connect(lambda : self.stoploss(self.T_3, self.qty_3, self.loss_3))
        self.SLoss_4.clicked.connect(lambda : self.stoploss(self.T_4, self.qty_4, self.loss_4))
        self.SLoss_5.clicked.connect(lambda : self.stoploss(self.T_5, self.qty_5, self.loss_5))
        #
        self.T_1.textChanged.connect(lambda : self.ticker_1.setText(self.T_1.toPlainText()))
        self.T_2.textChanged.connect(lambda : self.ticker_2.setText(self.T_2.toPlainText()))
        self.T_3.textChanged.connect(lambda : self.ticker_3.setText(self.T_3.toPlainText()))
        self.T_4.textChanged.connect(lambda : self.ticker_4.setText(self.T_4.toPlainText()))
        self.T_5.textChanged.connect(lambda : self.ticker_5.setText(self.T_5.toPlainText()))
        self.Arm.stateChanged.connect(self.arm)

    def buy(self, ticker, qty):
        self.statusBar.showMessage( "Pending..." )
        response = etradepy.buyNow( trading_account, ticker.toPlainText(), qty.toPlainText() )
        print response
        self.status_msg( response['PlaceEquityOrderResponse']['EquityOrderResponse']['messageList']['msgDesc'] )

    def sell(self, ticker, qty):
        self.status_msg( "Pending..." )
        response = etradepy.sellNow( trading_account, ticker.toPlainText(), qty.toPlainText() )
        print response
        self.status_msg( response['PlaceEquityOrderResponse']['EquityOrderResponse']['messageList']['msgDesc'] )

    def slimit(self, ticker, qty, price):
        self.status_msg( "Pending..." )
        response = etradepy.sellLimitNow( trading_account, ticker.toPlainText(), qty.toPlainText(),price.toPlainText() )
        print response
        self.status_msg( response['PlaceEquityOrderResponse']['EquityOrderResponse']['messageList']['msgDesc'] )

    def stoploss(self, ticker, qty, trailing):
        self.status_msg( "Pending..." )
        response = etradepy.sellStopNow( trading_account, ticker.toPlainText(), qty.toPlainText(),trailing.toPlainText() )
        print response
        self.status_msg( response['PlaceEquityOrderResponse']['EquityOrderResponse']['messageList']['msgDesc'] )

    def status_msg( self, message ):
        self.statusBar.showMessage( message )
        self.cleartimer.start(3000)

    def arm(self, int):
        state = self.Arm.isChecked()
        w = self.centralwidget
        p = w.palette()
        if state:
            p.setColor(w.backgroundRole(),QtGui.QColor(255,148,60))
        else:
            p.setColor(w.backgroundRole(),QtGui.QColor(73, 143, 255))
        w.setPalette(p)

        #
        self.Buy_1.setEnabled(state)
        self.Sell_1.setEnabled(state)
        self.SLimit_1.setEnabled(state)
        self.SLoss_1.setEnabled(state)
        #
        self.Buy_2.setEnabled(state)
        self.Sell_2.setEnabled(state)
        self.SLimit_2.setEnabled(state)
        self.SLoss_2.setEnabled(state)
        #
        self.Buy_3.setEnabled(state)
        self.Sell_3.setEnabled(state)
        self.SLimit_3.setEnabled(state)
        self.SLoss_3.setEnabled(state)
        #
        self.Buy_4.setEnabled(state)
        self.Sell_4.setEnabled(state)
        self.SLimit_4.setEnabled(state)
        self.SLoss_4.setEnabled(state)
        #
        self.Buy_5.setEnabled(state)
        self.Sell_5.setEnabled(state)
        self.SLimit_5.setEnabled(state)
        self.SLoss_5.setEnabled(state)


def main():
    global trading_account

    # start connection to etrade
    etradepy.login()
    accounts =  etradepy.listAccounts()
    trading_account = accounts['json.accountListResponse']['response'][0]['accountId']

    app = QtGui.QApplication(sys.argv)
    form = EtradeApp()
    form.show()
    form.statusBar.showMessage( accounts['json.accountListResponse']['response'][0]['accountDesc'])
    app.exec_()

if __name__ == '__main__':
    main()

