import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.CurrencyLogic import Currency
from ScreenDesign.clcScreen import clcScreen
from CurrencyCountry.findCurrency import FindCurrencyScreen
class UpdateScreen(clcScreen):
    @staticmethod
    def update_screen():
        clcScreen._DrawScreenHeader("\n\t\t\t\tUpdate Currency")
        input_value=FindCurrencyScreen.input_validaition("Code")
        if not Currency.is_exist(input_value):
            print("Currency code not found!")
            return
        
        search_code=Currency.find_by_country_code(input_value)
        FindCurrencyScreen.print_info(search_code)
        qoution=str(input("Are you sure to update rate (y/n)? ")).lower
        if qoution =="y":
            while True:
                try:
                    new_rate=float(input("\nEnter a new rate:"))
                    search_code.rate=new_rate
                    FindCurrencyScreen.print_info(search_code)
                    print("\nRate updated successfully!")
                    break
                except ValueError:
                    print("Invalid input! You must enter a float number!.") 
        else:
            return            
    