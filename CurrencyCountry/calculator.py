import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ScreenDesign.clcScreen import clcScreen
from core.CurrencyLogic import Currency
from CurrencyCountry.findCurrency import FindCurrencyScreen
class CalculatorRate(clcScreen):
    @staticmethod
    def AppleCalculator():
        clcScreen._DrawScreenHeader("\n\t\t\t\t\Calculator Currency")
        Continue=True
        while Continue:
            input_calculator_from=FindCurrencyScreen.input_validaition("a code country to calculator from it ")
            if Currency.is_exist(input_calculator_from):
                input_calculator_to=FindCurrencyScreen.input_validaition("a code country to calculator to it ")
                object_calculator_from=Currency.find_by_country_code(input_calculator_from)
                object_calculator_to=Currency.find_by_country_code(input_calculator_to)
                if Currency.is_exist(input_calculator_to):
                    try:
                        amount=float(input("\nEneter amount to Exchange: "))
                        equation_result_usd=float(amount/object_calculator_from.rate)
                        if input_calculator_to.lower() != "usd":
                            equation_result=equation_result_usd*object_calculator_to.rate
                            print("Convert from")
                            FindCurrencyScreen.print_info(object_calculator_from)
                            print("Conver to")
                            FindCurrencyScreen.print_info(Currency.find_by_country_code("usd"))
                            print("Conver to")
                            FindCurrencyScreen.print_info(object_calculator_to)
                            print(f"{amount} "
                                    f"{ object_calculator_from.currency_code} = "
                                    f"{equation_result} "
                                    f"{object_calculator_to.currency_code}")  
                            
                        else:
                            print("Convert from")
                            FindCurrencyScreen.print_info(object_calculator_from)
                            print("Conver to")
                            FindCurrencyScreen.print_info(object_calculator_to)
                            print(f"{amount} "
                                f"{ object_calculator_from.currency_code} = "
                                f"{equation_result_usd} "
                                f"{object_calculator_to.currency_code}")  
                        Continue=input("If you want to complete enter a True : ").capitalize()        
                    except ValueError:
                        print("It must be a float number try again! ") 
            else:
                print("the code country to convert to is not found try again! ")   
                if input("Clike enter to exit operation if you want it: ")=="":
                    return 
        else:    
            print("the code country to convert from is not found try again! ")
            if input("Clike enter to exit operation if you want it: ")=="":
                return    
                   
          
