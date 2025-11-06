import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clsBankClient import BankClient
from ScreenDesign.clcScreen import clcScreen
class ClcDepositSreccn:
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
    def sDeposit():   
        clcScreen._DrawScreenHeader("\tDeposit Screen")
        accountNum=input("\nEnter an account number! ")
        while not (BankClient.IsClientExist(accountNum)):
            print(f"\nClient with [ { accountNum} ] does not exist.\n")
            accountNum=input("\nEnter an account number! ")
        client1 =BankClient.Find(accountNum)
        ClcDepositSreccn._Print(client1)
        amount=float(input("\nPlease enter deposit amount?")) 
        choice=input("\nAre you sure you want to perform this transaction?").lower()
        if choice == "yes":
            client1.Deposit(amount)
            print("\nAmount Deposited Successfully.\n")
            print(f"\nNew Balance Is: {client1.AccountBalance}")  
        else:
            print("\nOperation was cancelled.\n")    
                      