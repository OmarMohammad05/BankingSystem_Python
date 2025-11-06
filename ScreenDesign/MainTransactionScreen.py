import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Transaction.TransferMoney import ScreenTransfer
from Transaction.DepositClass import ClcDepositSreccn
from Transaction.WithDraw import ClcWithDrawScreen 
from ClientFunctions.TotalBlaance import TotalBalance
from ScreenDesign.clcScreen import clcScreen
from core.clcUser import User
from enum import Enum
from Transaction.HistoyTransferScreen import HistoryTransfer
class clsTransactionsScreen():
    class __enTransactionsMenueOptions(Enum):
        eDeposit = 1
        eWithdraw = 2
        eShowTotalBalance = 3
        eTransfer=4
        eShowHistoryTransfet=5
        eShowMainMenue = 6
    @staticmethod
    def ReadTransactionsMenueOption():
        while True:
            print("Choose what do you want to do? [1 to 5]? ")
            choice=int(input("Enter Number between 1 to 5? "))
            if choice>=1 and choice<=5:
                return choice
            else:
                print("Try agin!") 
    @staticmethod
    def __ShowDepositScreen():
        ClcDepositSreccn.sDeposit()  
    @staticmethod
    def __ShowWithdrawScreen():
        ClcWithDrawScreen.sWithDraw()       
    @staticmethod
    def __ShowTotalBalancesScreen():
        TotalBalance.ShowTotalBalance()
    @staticmethod
    def __GoBackToTransactionsMenue():
        if input(f'{"":<0} \n\tPress any key to go back to Main Menue...\n')=="":    
            clsTransactionsScreen.ShowTransactionsMenue() 
    @staticmethod
    def __TransferMoney():
        ScreenTransfer.Transfer()   
    @staticmethod
    def __ShowHisoryTransfer():
        HistoryTransfer.ShowHistory()             
   
    @staticmethod
    def __PerformTransactionsMenueOption(TransactionsMenueOption:__enTransactionsMenueOptions):
        if TransactionsMenueOption == clsTransactionsScreen.__enTransactionsMenueOptions.eDeposit:
            clsTransactionsScreen.__ShowDepositScreen()
            clsTransactionsScreen.__GoBackToTransactionsMenue()
        elif TransactionsMenueOption == clsTransactionsScreen.__enTransactionsMenueOptions.eWithdraw:
            clsTransactionsScreen.__ShowWithdrawScreen()
            clsTransactionsScreen.__GoBackToTransactionsMenue()
        elif TransactionsMenueOption==clsTransactionsScreen.__enTransactionsMenueOptions.eShowTotalBalance:
            clsTransactionsScreen.__ShowTotalBalancesScreen()
            clsTransactionsScreen.__GoBackToTransactionsMenue()
        elif TransactionsMenueOption==clsTransactionsScreen.__enTransactionsMenueOptions.eTransfer:
            clsTransactionsScreen.__TransferMoney()
            clsTransactionsScreen.__GoBackToTransactionsMenue() 
        elif TransactionsMenueOption==clsTransactionsScreen.__enTransactionsMenueOptions.eShowHistoryTransfet:
            clsTransactionsScreen.__ShowHisoryTransfer()       
        elif TransactionsMenueOption == clsTransactionsScreen.__enTransactionsMenueOptions.eShowMainMenue:  
            print("do nothing here the main screen will handle it :-)")
            clsTransactionsScreen.__GoBackToTransactionsMenue()
    @staticmethod
    def ShowTransactionsMenue():
        if not clcScreen.CheckAccessRights(User.enPermission.pTransactionClient):
            return
        
        print("\t\t\t\t\t____________________________________________")
        clcScreen._DrawScreenHeader("\tTransactions Screen")
        print(" " * 20 + "===========================================")
        print(" " * 20 + "\t\t  Transactions Menu")
        print(" " * 20 + "===========================================")
        print(" " * 20 + "\t[1] Deposit.")
        print(" " * 20 + "\t[2] Withdraw.")
        print(" " * 20 + "\t[3] Total Balances.")
        print(" " * 20 + "\t[4] Transfer.")
        print(" " * 20 + "\t[5] History Transfer.")
        print(" " * 20 + "\t[6] Main Menu.")
        print(" " * 20 + "===========================================")   
        option=clsTransactionsScreen.ReadTransactionsMenueOption()
        enumOprtion=clsTransactionsScreen.__enTransactionsMenueOptions(option)
        clsTransactionsScreen.__PerformTransactionsMenueOption(enumOprtion)
      
         
