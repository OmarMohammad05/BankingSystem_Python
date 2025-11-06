import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LogInAndPermission.LogIn import LogInUser
if __name__ == "__main__":
    while True:
        if not LogInUser.ShowLogInScreen():
            break  
        
