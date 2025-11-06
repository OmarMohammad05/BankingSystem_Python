import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clsBankClient import BankClient
from core.clcUser import User
from ScreenDesign.clcScreen import clcScreen
class ScreenShowClientsList(clcScreen):
    @staticmethod
    def __PrintClientRecordList(client):
        print(f"| {client.AccountNumber:<12}"
            f"| {client.FullName():<20}"
            f"| {client.Phone:<15}"
            f"| {client.Email:<25}"
            f"| {client.PinCode:<10}"
            f"| {client.AccountBalance:<15}|")
    @staticmethod
    def ShowClientsList():
        if not clcScreen.CheckAccessRights(User.enPermission.pListClient):
            return
        clcScreen._DrawScreenHeader("List Client Screen")
        client=BankClient.GetListClient()
        print("\n__________________________________________________________________________________________________________")
        print(f"{'Account Number':<15} {'Full Name':<20} {'Phone':<15} {'Email':<25} {'Pin code':<10} {'Account Balance':<15}")
        print("__________________________________________________________________________________________________________\n") 
        if len(client) == 0:
            print("\t\t\tNo client available in the system!")
        else:
            for c in client:
                ScreenShowClientsList.__PrintClientRecordList(c)
                print()
        print("\n__________________________________________________________________________________________________________")

     