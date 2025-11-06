import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ScreenDesign.clcScreen import clcScreen
from core.clcUser import User
class ShowScreenRigester(clcScreen):
    @staticmethod
    def __Printer():
        print(f"{'UserName':<12}"
          f"| {'FirstName':<20}"
          f"| {'LastName':<15}"
          f"| {'Premissions':<20}"
          f"| {'Date':<12}"
          )

        
    @staticmethod
    def ShowRigesterScreen():
        if not clcScreen.CheckAccessRights(User.enPermission.pShowRigesterUser):
            return
        clcScreen._DrawScreenHeader("Register Screen")
        data=User.ListOfLogInRegister()
        ShowScreenRigester.__Printer()
        print("="*90)    

        if len(data) == 0 :
            print("NO use is registed ")
            return
            
        for user in data:
            print(f"{user['UserName']:<12}"
              f"| {user['FirstName']:<20}"
              f"| {user['LastName']:<15}"
              f"| {user['Premissions']:<20}"
              f"| {user['Date']:<12} |"
                  )
        print("\n\n", "="*90)
            
