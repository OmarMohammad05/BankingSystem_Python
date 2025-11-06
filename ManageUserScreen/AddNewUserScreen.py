import os ,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from core.clcUser import User
from ManageUserScreen.PermissionsClass import Permission
from ScreenDesign.clcScreen import clcScreen
class ScreenAddNewUser:
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
    def __ReadDataFromUser(userObj):
        dataMembers={"first name":"FirstName",
                     "last name":"LastName",
                     "email":"Email",
                     "phone":"Phone",
                     "password":"Password",
                     "permission":"Permissions" # After build it will convert to numerical values..
                     }
        for attr,val in dataMembers.items():
            if attr == "permission":
                setattr(userObj,val,Permission.Permissions())
            else: 
                value=input(f"Entre a {attr}: ")   
                setattr(userObj, val, value) 
    @staticmethod
    def AddUserScreen():
        clcScreen._DrawScreenHeader("\tAdd New User Screen")
        userName=input("Enter user name: ")
        while User.IsUserExist(userName):
            print("\nUser name already registered")
            userName=input("Enter user name or if you do not register click enter! ")
            if len(userName) ==0:
                print("Thank you!")
                return None
        if len(userName) !=0:  
            newUser=User.GetAddNewUserObject(userName)
            ScreenAddNewUser.__ReadDataFromUser(newUser)
            saveResult=newUser.Save()
            if saveResult == User.enSave.svSuccesed:
                print("Account added successfully - \n")
                ScreenAddNewUser.__Print(newUser)
            elif saveResult == User.enSave.svFaildEmptyObject:
                print("\n Error account was not saved because is empty:")
            elif saveResult == User.enSave.svUserExists:
                print("\n Error account is already used:") 