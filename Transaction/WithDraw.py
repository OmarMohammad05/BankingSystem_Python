import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clsBankClient import BankClient
from ScreenDesign.clcScreen import clcScreen
class ClcWithDrawScreen(clcScreen):
    @staticmethod
    def _Print(client):
        print("\nClient Card:")
        print(f"\nFirstName   : {client.FirstName}")
        print(f"\nLastName    : {client.LastName}")
        print(f"\nFull Name   : {client.FullName()}")
        print(f"\nEmail       : {client.Email}")
        print(f"\nPhone       : {client.Phone}")
        print(f"\nAcc. Number : {client._AccountNumber}")
        print(f"\nPassword    : {client._PinCode}")
        print(f"\nBalance     : {client._AccountBalance}")
        print("\n___________________\n")
  
    @staticmethod
    def sWithDraw():  
        clcScreen._DrawScreenHeader("\tWithDraw") 
        accountNum=input("\nEnter an account number! ")
        while  not (BankClient.IsClientExist(accountNum)):
            print(f"\nClient with [ { accountNum} ] does not exist.\n")
            accountNum=input("\nEnter an account number! ")
        client1 =BankClient.Find(accountNum)
        ClcWithDrawScreen._Print(client1)
        amount=float(input("\nPlease enter withdraw amount?")) 
        choice=input("\nAre you sure you want to perform this transaction?").lower()
        if choice == "yes":
            if client1.Withdraw(amount):
                print("\nAmount Withdrawed Successfully.\n")
                print(f"\nNew Balance Is: {client1.AccountBalance}")  
            else:
                print("\nInsufficient Balance.\n")    
        else:
            print("\nOperation was cancelled.\n")