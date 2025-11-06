import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from ScreenDesign.clcScreen import clcScreen
from ManageUserScreen.PermissionsClass import Permission
from core.clcUser import User
from core.SecurityPasswrod import Security
class UpdateUser(clcScreen):
    @staticmethod
    def __Print(userObj):
        print("\nUser Card:")
        print(f"\nFirstName   : {userObj.FirstName}")
        print(f"\nLastName    : {userObj.LastName}")
        print(f"\nEmail       : {userObj.Email}")
        print(f"\nPhone       : {userObj.Phone}")
        print(f"\nUserName    : {userObj.UserName}")
        print(f"\nPassword    : {userObj.Password}")
        print(f"\nPermissions : {userObj.Permissions}")
        print("\n___________________\n")
    @staticmethod
    def __ReadInfo(user_obj):
        dataMember={
            "first name":"FirstName",
            "last name": "LastName",
            "email":"Email",
            "phone":"Phone",
            "user name":"UserName",
            "password":"Password",
            "permission":"Permissions"
        } 
        while True:
            choose=input("\nEnter the field you want to update (all/exit):").lower()
            if choose == "exit":
                break
            elif choose=="all":
                for attr,val in dataMember.items():
                    if attr == "permission":
                        value=Permission.Permissions()
                    elif attr == "password":
                        value=input(f"Enter a password:")
                        value=Security.Encryp(value,5)
                    else:
                        value=input(f"Enter {attr}: ")
                    setattr(user_obj,val ,value)   
                        
            elif choose in dataMember:
                if choose == "permission":
                    value=Permission.Permissions()
                elif choose == "password":
                    value=input(f"Enter a password:")
                    value=Security.Encryp(value,5)
                else:
                    value=input(f"\n Enter {choose}: ")        
                setattr(user_obj,dataMember[choose], value) 
            else:
                print("Try again! ")    
                
    @staticmethod
    def UpdateUserScreen():
        clcScreen._DrawScreenHeader("\tUpdate User Screen ")
        user_name=input("Enter a user name: ")
        while not  User.IsUserExist(user_name):
            user_name=input("The user name is not found try again!: ")
        user=User.Find(user_name)
        UpdateUser.__Print(user)
        UpdateUser.__ReadInfo(user)
        saveResult=user.Save()
        if saveResult == User.enSave.svFaildEmptyObject:
            print("User is empty, cannot save!")
        elif saveResult == User.enSave.svSuccesed:
            print("Client saved successfully!")    
            UpdateUser.__Print(user)

            
         


