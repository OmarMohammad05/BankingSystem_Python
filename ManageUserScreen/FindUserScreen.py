import os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from core.clcUser import User
from ScreenDesign.clcScreen import clcScreen
class FindUserScreen(clcScreen):
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
    def FindUser():
        clcScreen._DrawScreenHeader("\t Find User Screen ")
        user_name=input("Enter a UserName: ") 
        while not User.IsUserExist(user_name):
            user_name=input("The userName is not found try again!: ")
        userFind=User.Find(user_name)
        if userFind.IsEmpty():
            print("The user name is empty: ")
        else:
            FindUserScreen.__Print(userFind) 
                    

