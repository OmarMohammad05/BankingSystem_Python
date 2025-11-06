import os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from core.clsBankClient import BankClient
from ScreenDesign.clcScreen import clcScreen

class ScreenFindClient(clcScreen):
    @staticmethod
    def __Print(client_obj):
        print("\nUser Card:")
        print(f"\nFirstName   : {client_obj.FirstName}")
        print(f"\nLastName    : {client_obj.LastName}")
        print(f"\nEmail       : {client_obj.Email}")
        print(f"\nPhone       : {client_obj.Phone}")
        print(f"\nAccountNumber    : {client_obj.AccountNumber}")
        print(f"\nPinCode    : {client_obj.PinCode}")
        print(f"\nAccountBalance: {client_obj.AccountBalance}")
        print("\n___________________\n")
    @staticmethod
    def find_client_screen():
        clcScreen._DrawScreenHeader("\t Find Clinet Screen ")
        acc_num=input("Enter a account number: ") 
        while not BankClient.IsClientExist(acc_num):
            acc_num=input("The account number is not found try again!: ")
        client_find=BankClient.Find(acc_num)
        if client_find.IsEmpty():
            print("The account number is empty: ")
        else:
            ScreenFindClient.__Print(client_find) 
