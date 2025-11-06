import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CurrencyCountry.calculator import CalculatorRate
from ScreenDesign.clcScreen import clcScreen
from enum import Enum
from CurrencyCountry.ListSceeen import ListCurrenciesScreen
from CurrencyCountry.findCurrency import FindCurrencyScreen
from CurrencyCountry.update_rate import UpdateScreen
class MainScreen(clcScreen):
    class eCurrency(Enum):
        list_currency=1
        find_currecny=2
        update_currecny=3
        currency_claculate=4
        main_menu=5
    @staticmethod
    def _ReadMainMenueOption():
        """
         Prompts the user to select an option between 1 and 5.

        Returns:
            int: The user's selected option.
    """
        print(f'{"":<0}Choose what do you want to do? [1 to 5]? ')
        while True:
            try:
                choice=int(input("Enter a number between 1 to 5 :"))
                if 1 <= choice <= 5:
                    return choice
                else:
                    print(" Please enter a number between 1 and 5.\n")
            except (ValueError,TypeError):
                raise ValueError(" Invalid input. Please enter an integer number.\n")    
    @staticmethod
    def __GoBackToMainMenue():
        clike=input(f'{"":<0} \n\tPress any key to go back to Main Menue...\n ')
        if clike == "":
            MainScreen.showMainMenu()
    @staticmethod
    def __show_currency_list():
        ListCurrenciesScreen.show_list_currency()        
    @staticmethod
    def __find_currency():
        FindCurrencyScreen.find_currency_screen()
    @staticmethod
    def __update():
        UpdateScreen.update_screen()                
    @staticmethod
    def __currenct_claculator():
        CalculatorRate.AppleCalculator()
    @staticmethod
    def __main_menu():
        #clcMainScreen._GoBackToMainMenue() 
        pass
  
    @staticmethod
    def __Perform_currency_menue_option(currency_option:eCurrency):
        if currency_option == MainScreen.eCurrency.list_currency:
            MainScreen.__show_currency_list()
            MainScreen.__main_menu()
        elif currency_option == MainScreen.eCurrency.find_currecny:
            MainScreen.__find_currency() 
            MainScreen.__main_menu()
        elif currency_option==MainScreen.eCurrency.update_currecny:
            MainScreen.__update()
            MainScreen.__main_menu()
        elif currency_option == MainScreen.eCurrency.currency_claculate:
            MainScreen.__currenct_claculator()
            MainScreen.__main_menu()
        elif currency_option == MainScreen.eCurrency.main_menu:
            MainScreen.__main_menu()        
    @staticmethod
    def ShowManageUserScreen():
        clcScreen._DrawScreenHeader("Currency Exchange Main Screen")
        print(" " * 20 + "===========================================")
        print(" " * 20 + "\t\t Currency Exchange Menue")
        print(" " * 20 + "===========================================")
        print(" " * 20 + "\t[1] List Currenct.")
        print(" " * 20 + "\t[2] Find Currency.")
        print(" " * 20 + "\t[3] Update Currency.")
        print(" " * 20 + "\t[4] Currency calculator.")
        print(" " * 20 + "\t[5] Main Menu.")
        print(" " * 20 + "===========================================") 
        option=MainScreen._ReadMainMenueOption()
        en_opetion=MainScreen.eCurrency(option)
        MainScreen.__Perform_currency_menue_option(en_opetion)
