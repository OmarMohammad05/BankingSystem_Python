import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clsBankClient import BankClient
from ScreenDesign.clcScreen import clcScreen
from Transaction.TransferMoney import ScreenTransfer
import json
class HistoryTransfer(clcScreen):
    @staticmethod
    def __Printer():
        print(
          f"{'Date':<20}"
          f"| {'s.acc_num':<15}"
          f"| {'d.acc_num':<12}"
          f"| {'Amount':<15}"
          f"| {'S.balance':<10}"
          f"| {'d.balance':<10}"
          f"| {'User':<10}"
          )
        print("-"*100,"\n")
    @staticmethod
    def ShowHistory():
        clcScreen._DrawScreenHeader("History Transfer")
        path=ScreenTransfer._Path()
        data=list()
        HistoryTransfer.__Printer()
        with open(path,"r") as file:
            data=json.load(file)
        for clien in data:
            print(f"{clien['Date']:<20}"
              f"| {clien['Source acc num']:<15}"
              f"| {clien['Destination acc num']:<12}"
              f"| {clien['Amount tranfer']:<15}"
              f"| {clien['Source balance']:<10} "
              f"| {clien['Destination balance']:<10}"
              f"| {clien['User']:<10} |"
                  )    
        print("-" * 110)
    

            
        
