import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from core.clcUser import User
import Global
from ScreenDesign.MainScreen import clcMainScreen
from ScreenDesign.clcScreen import clcScreen
from core.SecurityPasswrod import Security
class LogInUser:
    @staticmethod
    def __LogIn():
        clcScreen._DrawScreenHeader("\tLog In Screen ")
        log_in=True
        count=3
        while log_in:
            log_in=False
            user_name=input("Enter a user name: ")
            password=input("Enter a password: ")
            Global.current_user=User.Find(user_name,password)
            log_in=Global.current_user.IsEmpty()
            if log_in:
                count-=1 
                print("\nInvlaid userName\\password")  
                print(f"\n You have {count} times")
                if count == 0:
                    print("Your are locked after 3 faild trail")
                    return False
            if count >0 and not log_in:
                Global.current_user.RegisterLogIn()
                clcMainScreen.showMainMenu()                    
    @staticmethod
    def ShowLogInScreen():
        return LogInUser.__LogIn()
            
            
        
           