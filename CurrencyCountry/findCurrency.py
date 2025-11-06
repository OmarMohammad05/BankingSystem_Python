import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ScreenDesign.clcScreen import clcScreen
from core.CurrencyLogic import Currency
class FindCurrencyScreen(clcScreen):
    @staticmethod
    def print_info(currency_object):
        if not currency_object:
            print("Currency not found.")
            return
        print("\n___________________\n")
        print(f"\nName Country   : {currency_object.name_country}")
        print(f"\nCurrency Name    : {currency_object.currency_name}")
        print(f"\nCurrency Code       : {currency_object.currency_code}")
        print(f"\nRate       : {currency_object.rate}")
        print("\n___________________\n")
    @staticmethod
    def input_validaition(type_input:str):
        try:
            while True:
                user_input=str(input(f"\nEnter a {type_input}: "))
                if  Currency.is_exist(user_input):
                    return user_input
                else:
                    print(f"{type_input} not found. Please try again.")
        except Exception as e:
            print(f"Error {e}")
            return None            
    @staticmethod
    def find_currency_screen():
        clcScreen._DrawScreenHeader("\n\t\t\t\t\tFind Currency")
        while True:
            try:
                choice=int(input("\nFind by: [1] code or [2] Country or [0] if you want exit: "))
                if choice==0:
                    print("Exit...")
                    break
                elif choice ==1:
                    search_input=FindCurrencyScreen.input_validaition("Code")
                    object_code_find=Currency.find_by_country_code(search_input)
                    print("\nCurrency Object:")
                    FindCurrencyScreen.print_info(object_code_find)
                    return
                elif choice == 2:
                    search_input=FindCurrencyScreen.input_validaition("Country")
                    object_country_find=Currency.find_by_country_name(search_input)
                    print("\nCurrency Object:")
                    FindCurrencyScreen.print_info(object_country_find)
                    return
                else:
                    print("You must enter a number 1 or 2 just.")    
            except ValueError:
                raise TypeError("You must enter a number:")       
                        
            