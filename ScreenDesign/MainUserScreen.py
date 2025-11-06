import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from ManageUserScreen.ShowUserListScreen import ListOfUser
from enum import Enum
from ManageUserScreen.AddNewUserScreen import ScreenAddNewUser
from ManageUserScreen.DeleteUserScreen import DeleteUser
from ManageUserScreen.UpdateUerScreen import UpdateUser
from ManageUserScreen.FindUserScreen import FindUserScreen
from core.clcUser import User
from ScreenDesign.clcScreen import clcScreen
class clcManageUserScreen:
    class _eManageUserScreenOptions(Enum):
        eListUsers = 1
        eAddNewUser = 2
        eDeleteUser = 3
        eUpdateUser = 4
        eFindUser = 5
        eMainMenu = 6
    @staticmethod    
    def __ReadManageUserScreenOption():
        while True:
            print("Choose what do you want to do? [1 to 6]? ")
            choice=int(input("Enter Number between 1 to 6? "))
            if choice>=1 and choice<=6:
                return choice
            else:
                print("Try again!")
    @staticmethod
    def __GoBackToManageUserScreen():
        if input("\nClike Enter if you want to back main meun: ") == "":
            clcManageUserScreen.ShowManageUserScreen()
    @staticmethod
    def __ShowListUsersScreen():
        ListOfUser.ShowUserList()
    @staticmethod
    def __ShowAddNewUserScreen():
        ScreenAddNewUser.AddUserScreen()
    @staticmethod
    def __ShowDeleteUserScreen():
        DeleteUser.DeleteUserScreen()
    @staticmethod
    def __ShowUpdateUserScreen():
        UpdateUser.UpdateUserScreen()        
    @staticmethod
    def __ShowFindUserScreen():
        FindUserScreen.FindUser()             
    
    @staticmethod
    def __PerformManageUserScreenOption(ManageUserScreenOption: _eManageUserScreenOptions):
        if ManageUserScreenOption == clcManageUserScreen._eManageUserScreenOptions.eListUsers:
            clcManageUserScreen.__ShowListUsersScreen()
            clcManageUserScreen.__GoBackToManageUserScreen()
        elif ManageUserScreenOption == clcManageUserScreen._eManageUserScreenOptions.eAddNewUser:
            clcManageUserScreen.__ShowAddNewUserScreen()
            clcManageUserScreen.__GoBackToManageUserScreen()
        elif ManageUserScreenOption == clcManageUserScreen._eManageUserScreenOptions.eDeleteUser:  
            clcManageUserScreen.__ShowDeleteUserScreen()
            clcManageUserScreen.__GoBackToManageUserScreen()
        elif ManageUserScreenOption == clcManageUserScreen._eManageUserScreenOptions.eUpdateUser:
            clcManageUserScreen.__ShowUpdateUserScreen()
            clcManageUserScreen.__GoBackToManageUserScreen()
        elif ManageUserScreenOption == clcManageUserScreen._eManageUserScreenOptions.eFindUser:
            clcManageUserScreen.__ShowFindUserScreen()
            clcManageUserScreen.__GoBackToManageUserScreen()
        elif ManageUserScreenOption==clcManageUserScreen._eManageUserScreenOptions.eMainMenu:
            print("E main Meun")
    @staticmethod
    def ShowManageUserScreen():
        if not clcScreen.CheckAccessRights(User.enPermission.pManageUsers):
            return
        print(" " * 20 + "===========================================")
        print(" " * 20 + "\t\t Manage User Menu")
        print(" " * 20 + "===========================================")
        print(" " * 20 + "\t[1] List User.")
        print(" " * 20 + "\t[2] Add New USer.")
        print(" " * 20 + "\t[3] Delete User.")
        print(" " * 20 + "\t[4] Update User.")
        print(" " * 20 + "\t[5] Find User.")
        print(" " * 20 + "\t[6] Main Menu.")
        print(" " * 20 + "===========================================") 
        option=clcManageUserScreen.__ReadManageUserScreenOption()
        enOption=clcManageUserScreen._eManageUserScreenOptions(option)
        clcManageUserScreen.__PerformManageUserScreenOption(enOption)


                                  
                
    