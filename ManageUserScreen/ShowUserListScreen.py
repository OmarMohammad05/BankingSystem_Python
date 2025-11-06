
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from core.clcUser import User
from ScreenDesign.clcScreen import clcScreen
class ListOfUser:
    @staticmethod
    def __Print(userObject):
        print(f"|{userObject.FirstName:<15}"
            f"| {userObject.LastName:<20}"
            f"| {userObject.Email:<15}"
            f"| {userObject.Phone:<25}"
            f"| {userObject.UserName:<10}"
            f"| {userObject.Password:<15}"
            f"| {userObject.Permissions:<15}")
    @staticmethod
    def ShowUserList():
        ListUser=User.GetUsersList()
        clcScreen._DrawScreenHeader("\tUser List")
        print("\n_______________________________________________________________________________________________________________________")
        print(f"{'FirstName':<15} {'LastName':<20} {'Email':<15} {'Phone':<25} {'User Name':<10} {'Password':<15} {'Permissions':<15}")
        print("_______________________________________________________________________________________________________________________\n") 
        if len(ListUser)==0:
            print("\t\tNO user available:")
        else:    
            for us in ListUser:
                ListOfUser.__Print(us)
                
        print("\n_________________________________________________________________________________________________________________________")
        