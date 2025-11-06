# MainScreen
import sys
import os
from ClientFunctions.find_client import ScreenFindClient
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ClientFunctions.AddClient import ScreenAddClient
from ClientFunctions.ShowClientList import ScreenShowClientsList
from ClientFunctions.DeleteClient import ScreenDeleteClient
from ClientFunctions.UpdateClient import ScreenUpdateClient
from ScreenDesign.MainTransactionScreen import clsTransactionsScreen
from ScreenDesign.MainUserScreen import clcManageUserScreen
from enum import Enum
import Global
from core.clcUser import User
from ScreenDesign.clcScreen import clcScreen
from LogInAndPermission.RigesterData import ShowScreenRigester
from ScreenDesign.MainScreenCurrencies import MainScreen
class clcMainScreen(clcScreen):
    class _enMainMenueOptions(Enum):
        eListClients = 1 
        eAddNewClient = 2
        eDeleteClient = 3
        eUpdateClient = 4
        eFindClient = 5
        eShowTransactionsMenue = 6
        eManageUsers = 7
        eLogInRegister=8
        eCurrencyData=9
        eExit = 10
    @staticmethod
    def _ReadMainMenueOption():
        """
         Prompts the user to select an option between 1 and 10.

        Returns:
            int: The user's selected option.
    """
        print(f'{"":<0}Choose what do you want to do? [1 to 10]? ')
        while True:
            try:
                choice=int(input("Enter a number between 1 to 10 :"))
                if 1 <= choice <= 10:
                    return choice
                else:
                    print(" Please enter a number between 1 and 10.\n")
            except (ValueError,TypeError):
                raise ValueError(" Invalid input. Please enter an integer number.\n")    
    @staticmethod
    def _GoBackToMainMenue():
        clike=input(f'{"":<0} \n\tPress any key to go back to Main Menue...\n ')
        if clike == "":
            clcMainScreen.showMainMenu()
    @staticmethod
    def _ShowAllClientsScreen():
        ScreenShowClientsList.ShowClientsList()
    @staticmethod
    def _ShowAddNewClientsScreen():
        ScreenAddClient.AddNewClient()
    @staticmethod
    def _ShowDeleteClientScreen():
        ScreenDeleteClient.DeleteClient()
    @staticmethod
    def _ShowUpdateClientScreen():
        ScreenUpdateClient.UpdateClient()
    @staticmethod
    def _ShowFindClientScreen():
        ScreenFindClient.find_client_screen()                   
    @staticmethod
    def _ShowTransactionsMenue():
        clsTransactionsScreen.ShowTransactionsMenue()
    @staticmethod
    def _ShowManageUsersMenue():
        clcManageUserScreen.ShowManageUserScreen()             
    @staticmethod
    def _LogOut():
        Global.current_user=User.Find("","")
    @staticmethod
    def __LogInRegister():
        ShowScreenRigester.ShowRigesterScreen()     
    @staticmethod
    def __currncey_data():
        MainScreen.ShowManageUserScreen()           
            
    @staticmethod
    def performMainMenuOption(option: _enMainMenueOptions):
        if option ==  clcMainScreen._enMainMenueOptions.eListClients:
            clcMainScreen._ShowAllClientsScreen()
            clcMainScreen._GoBackToMainMenue()
        elif option ==  clcMainScreen._enMainMenueOptions.eAddNewClient:
             clcMainScreen._ShowAddNewClientsScreen()
             clcMainScreen._GoBackToMainMenue()
        elif option ==  clcMainScreen._enMainMenueOptions.eDeleteClient:
             clcMainScreen._ShowDeleteClientScreen()
             clcMainScreen._GoBackToMainMenue()
        elif option ==  clcMainScreen._enMainMenueOptions.eUpdateClient:
             clcMainScreen._ShowUpdateClientScreen()
             clcMainScreen._GoBackToMainMenue()
        elif option ==  clcMainScreen._enMainMenueOptions.eFindClient:
            clcMainScreen._ShowFindClientScreen()
            clcMainScreen._GoBackToMainMenue()
        elif option ==  clcMainScreen._enMainMenueOptions.eShowTransactionsMenue:
            clcMainScreen._ShowTransactionsMenue()
            clcMainScreen._GoBackToMainMenue()
        elif option ==  clcMainScreen._enMainMenueOptions.eManageUsers:
            clcMainScreen._ShowManageUsersMenue()
            clcMainScreen._GoBackToMainMenue()
        elif option== clcMainScreen._enMainMenueOptions.eLogInRegister:
            clcMainScreen.__LogInRegister()
            clcMainScreen._GoBackToMainMenue()   
        elif option == clcMainScreen._enMainMenueOptions.eCurrencyData:
            clcMainScreen.__currncey_data()
            clcMainScreen._GoBackToMainMenue() 
        elif option ==  clcMainScreen._enMainMenueOptions.eExit:
            clcMainScreen._LogOut()
    @staticmethod       
    def showMainMenu():
        clcScreen._DrawScreenHeader("\t\tMain Screen")
        print(f'{"":<0}===========================================')
        print(f'{"":<0}\t\tMain Menu')
        print(f'{"":<0}===========================================')
        print(f'{"":<0}\t[1] Show Client List.')
        print(f'{"":<0}\t[2] Add New Client.')
        print(f'{"":<0}\t[3] Delete Client.')
        print(f'{"":<0}\t[4] Update Client Info.')
        print(f'{"":<0}\t[5] Find Client.')
        print(f'{"":<0}\t[6] Transactions.')
        print(f'{"":<0}\t[7] Manage Users.')
        print(f'{"":<0}\t[8] Log in Register.')
        print(f'{"":<0}\t[9] Currency Exchange.')
        print(f'{"":<0}\t[10] Logout.')
        print(f'{"":<0}===========================================')

        option =clcMainScreen._ReadMainMenueOption()
        enum_option = clcMainScreen._enMainMenueOptions(option)   # تحويل int → Enum
        clcMainScreen.performMainMenuOption(enum_option)

   

           