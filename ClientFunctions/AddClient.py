import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clsBankClient import BankClient
from ClientFunctions.ReadClientInfo import ReadClientInfo
from ScreenDesign.clcScreen import clcScreen
from core.clcUser import User


class ScreenAddClient(clcScreen):
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
    def AddNewClient():
        if not clcScreen.CheckAccessRights(User.enPermission.pAddNewClinet):
            return
        clcScreen._DrawScreenHeader("\tAdd new Client Screen")
        accountNumber=input("\n Enter Account number: ")
        while BankClient.IsClientExist(accountNumber):
            print("Account numner is already used , choose anthor one: ")
            accountNumber=input("\n Enter Account number: ")
        newClient=BankClient.GetAddNewClientObject(accountNumber)
        ReadClientInfo.ReadClient(newClient)  
        saveResult=newClient.Save()
        if saveResult==BankClient.SaveResult.svSucceeded:
            print("Account added successfully - \n")
            ScreenAddClient._Print(newClient)
        elif saveResult == BankClient.SaveResult.svFailedEmptyObject:
            print("\n Error account was not saved because is empty:")
        elif saveResult == BankClient.SaveResult.svFailedNumberExists:
            print("\n Error account is already used:") 
