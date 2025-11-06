import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clsBankClient import BankClient
from ScreenDesign.clcScreen import clcScreen
from core.clcUser import User
class ScreenDeleteClient(clcScreen):
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
    def DeleteClient():
        if not clcScreen.CheckAccessRights(User.enPermission.pDeleteClinet):
            return
        clcScreen._DrawScreenHeader("\tDelete Client Screen")
        AccountNumber=input("\n Enter an account number: ")
        while not BankClient.IsClientExist(AccountNumber):
            print("\n The client number is not found enter other number: ")
            AccountNumber=input("\n Enter an account number: ")
        client1=BankClient.Find(AccountNumber)
        ScreenDeleteClient._Print(client1)
        answer=input("\n Are you sure you want to delete this client y/n: ").lower() 
        if answer == 'y':
            client1=client1.delete()
            if client1.IsEmpty():
                print(" Client deleted Successfully")
                ScreenDeleteClient._Print(client1)
            else:
                print("\n Error client was not deleted")   
                

