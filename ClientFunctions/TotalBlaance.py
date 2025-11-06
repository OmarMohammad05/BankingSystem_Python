import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clsBankClient import BankClient
class TotalBalance:
    @staticmethod   
    def ShowTotalBalance():
        clients=BankClient.GetListClient()
        total=BankClient.GetTotalBalance()
        print(f"\n\t\t\t\tBalances List {len(clients)} Clinet(s)")
        print("\n_____________________________________________________________________________")
        print(f"|{'Account Number':<20} |{'Full Name':<20} |{'Account Balance':<15}")
        print("\n_____________________________________________________________________________") 
        if len(clients)==0:
            print("\t\t\tNo client available in the system!")
        else:
         for client in clients:
            print(f"| {client.AccountNumber:<20}"
          f"| {client.FullName():<20}"
          f"| {client.AccountBalance:<15}")
            print()
        print("\n__________________________________________________________________________________________________________")
                    
        print(f"\n\t\t\t\t\tTotal Balances= {total}")
 
 