import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ScreenDesign.clcScreen import clcScreen
from core.clsBankClient import BankClient
from datetime import datetime
import json
import Global

class ScreenTransfer(clcScreen):
    @staticmethod
    def __PrintInfo(client_obj):
        print("\n\nClient Card: ")
        print("-"*50)
        print(f"Full Name : {client_obj.FullName()}")
        print(f"Acc.Numner : {client_obj.AccountNumber}")
        print(f"Balance : {client_obj.AccountBalance}")
        print("-"*50,"\n")
    @staticmethod
    def __ReadAccountNumber():
        account_num=input("Please Enter Account Numeber to transfer from: \n")
        while not BankClient.IsClientExist(account_num):
            account_num=input("This is not found this account number please try again: "
                                        "If you want to exit clike enter: \n")
            if account_num=="":
                return
        return account_num     
            
    @staticmethod
    def Transfer(): 
        source_acc=ScreenTransfer.__ReadAccountNumber() 
        scource_client= BankClient.Find(source_acc) 
        ScreenTransfer.__PrintInfo(scource_client)
        
        destination_acc=ScreenTransfer.__ReadAccountNumber()
        destination_client=BankClient.Find(destination_acc)
                
            
        if destination_acc == source_acc:
            print(" You can\’t make a transaction to the same account.\n")   
        else:         
            destination_client=BankClient.Find(destination_acc)
            ScreenTransfer.__PrintInfo(destination_client)
            
            amount_tranfer=float(input("Enter Transfer amount: "))
            can_withdraw=scource_client.Withdraw(amount_tranfer)
            
            if not can_withdraw:
                print("You don\’t have enough balance")
            else:
                
                if input("Are you sure you want to perform this operation? (y//n): ").lower()=="y":
                    destination_client.Deposit(amount_tranfer)
                    print("\nTransfer done successfully.\n")
                    ScreenTransfer.__PrintInfo(scource_client)
                    ScreenTransfer.__PrintInfo(destination_client)
                    ScreenTransfer.__SaveHistoryTranfer(scource_client,destination_client,amount_tranfer)
                    print("\nThank you!")
            return
    @staticmethod
    def __DataStructure(source_obj,destination_obj,amount_tranfer):
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_for_save={
                "Date":date_str,
                "Source acc num":source_obj.AccountNumber,
                "Destination acc num":destination_obj.AccountNumber,
                "Amount tranfer":amount_tranfer,
                "Source balance":source_obj.AccountBalance ,
                "Destination balance":destination_obj.AccountBalance ,
                "User": Global.current_user.UserName
            }
        return data_for_save
        
    @staticmethod
    def _Path():
        path=os.path.join('data','TransferLog.json')
        if os.path.exists(path):
            return path
        else:
            print("The path not exists!")
        
    @staticmethod
    def __SaveHistoryTranfer(source_obj,destination_obj,amount_tranfer):
        path=ScreenTransfer._Path()
        data=ScreenTransfer.__DataStructure(source_obj,destination_obj,amount_tranfer)
        all_data=list()
        with open(path,"r") as file:
            try:
                all_data=json.load(file)
                if isinstance(all_data,dict):
                    all_data=[all_data]
            except json.JSONDecodeError:
                all_data=[]
        all_data.append(data)
        with open(path,"w") as file:
            json.dump(all_data,file,indent=4)    
                    
            
            
    