import os , sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from core.clcUser import User
from ScreenDesign.clcScreen import clcScreen
class DeleteUser(clcScreen):
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
    def DeleteUserScreen():
        clcScreen._DrawScreenHeader("\tDelete screen")
        user_name=input("Enter a user name: ")
        while  not User.IsUserExist(user_name):
            user_name=input("The user name is not found try again! :")
        user=User.Find(user_name)
        DeleteUser.__Print(user)
        chose=input("Are you sure to delete the user (y/n)? ").lower()
        if chose=="y":
            user=user.Delete()
            if user.IsEmpty():
                print(" Client deleted Successfully")
                DeleteUser.__Print(user)    
        else:
           print("\n Error client was not deleted")      
            
            
         