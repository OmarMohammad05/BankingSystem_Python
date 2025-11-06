import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clcUser import User
import Global
from datetime import date
class clcScreen:
    @staticmethod
    def _DrawScreenHeader(title , subTitel=None):
        os.system('cls' if os.name == 'nt' else 'clear')
        today=date.today()
        print("=================================================================================================")
        print("\n\n\t\t\t\t",title)
        print(f"UserName:{Global.current_user.UserName}")
        print(f"Date:{today}")
        if subTitel is not None:
            print("\n\t\t\t\t\t ",subTitel)
        print("\n\n=================================================================================================")
    @staticmethod
    def CheckAccessRights(permission:User.enPermission):
        if not Global.current_user.CheckAccessPermission(permission):
            print("\t=========================================================================================")
            print("\n\n\t\tAccess Denied! Contact your Admin.")
            print("\n\t=======================================================================================\n\n")
            return False
        else:
            return True

        
           
