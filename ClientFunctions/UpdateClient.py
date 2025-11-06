import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clsBankClient import BankClient
from ClientFunctions.ReadClientInfo import ReadClientInfo
from core.clcUser import User
from ScreenDesign.clcScreen import clcScreen
class ScreenUpdateClient(clcScreen):
    @staticmethod
    def __PrintClientRecordList(client):
        print(f"| {client.AccountNumber:<12}"
            f"| {client.FullName():<20}"
            f"| {client.Phone:<15}"
            f"| {client.Email:<25}"
            f"| {client.PinCode:<10}"
            f"| {client.AccountBalance:<15}|")
    def UpdateClient():
        """_summary_
        To search account number and found in data base 
        and put in object pass to the function ReadClientInfo to updated info.
        """
        if not clcScreen.CheckAccessRights(User.enPermission.pUpdateClinet):
            return
        clcScreen._DrawScreenHeader("\tUpdate Client Screen")
        accountNumber=str(input("\n Please enter client account number: "))
        while not BankClient.IsClientExist(accountNumber):
            print("\n Account number is not found , choose another one: ")
            accountNumber=str(input("\n Please enter client account number: "))

        client1=BankClient.Find(accountNumber)
        ScreenUpdateClient.__PrintClientRecordList(client1)  
        print("\n\n Update client info")
        print("\n__________________________________\n")
        ReadClientInfo.ReadClient(client1)
        saveResult=client1.Save()
        if saveResult == BankClient.SaveResult.svFailedEmptyObject:
            print("Client is empty, cannot save!")
        elif saveResult == BankClient.SaveResult.svSucceeded:
            print("Client saved successfully!")
