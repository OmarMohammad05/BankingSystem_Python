import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ScreenDesign.clcScreen import clcScreen
from core.CurrencyLogic import Currency
class ListCurrenciesScreen(clcScreen):
    @staticmethod
    def __print_currency(currency_object):
            print(
            f"|{currency_object.currency_name:<15}"
            f"| {currency_object.name_country:<25}"
            f"| {currency_object.currency_code:<20}"
            f"| {currency_object.rate:<20}")
    @staticmethod        
    def show_list_currency():
        clcScreen._DrawScreenHeader("\t List Currency")
        list_currencies=Currency.get_currency_list()
        print("\n_______________________________________________________________________________________________________________________")
        print(f"{'Currency Name':<15} {'Name Country':<25} {'Currency code':<20} {'Rate':<20}")
        print("_______________________________________________________________________________________________________________________\n") 
        if len(list_currencies)==0:
            return("\t\tNO user available:")
        for index in list_currencies:
            ListCurrenciesScreen.__print_currency(index)
        print("\n_________________________________________________________________________________________________________________________")
            
            
