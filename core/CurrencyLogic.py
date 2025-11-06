import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from enum import Enum
import os
class Currency:
    __DATA_DIR = "data"
    __FILE_NAME = "Currencies.txt"
    class __c_mode(Enum):
        """_summary_
        const number to know which operated.

        Args:
            Enum (intger): _currenct empty  and currency update._
        """
        c_empty=0
        c_update=1
    def __init__(self,new_name_country:str,new_currency_code:str,new_currency_name,new_rate:float,new_mode:__c_mode):
        """
    Initializes a Currency object with its main properties.

    Args:
        new_name_country (str): Name of the country.
        new_currency_name (str): Name of the currency (e.g., Dinar).
        new_currency_code (str): Currency code (e.g., JOD).
        new_rate (float): Exchange rate relative to base currency.
        new_mode (__c_mode): Mode of the currency (empty/update).
        """
        self.__name_country=new_name_country
        self.__currency_code=new_currency_code
        self.__currency_name=new_currency_name
        self.__rate=new_rate
        self.__mode=new_mode
    @staticmethod
    def __path_file():
        """_summary_
        
        This methode jsut take a path of file.

        Raises:
            FileNotFoundError: file not fount.

        Returns:
            _type_: path of data base.
        """
        path=os.path.join(Currency.__DATA_DIR,Currency.__FILE_NAME)
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found {path} ")
        return path
    @property
    def currency_name(self)->str:
        """_summary_
        just return a value of property class.
        Returns:
            str: value from object_line have a currecny name.
        """
        return self.__currency_name
    @property
    def name_country(self) ->str:
        """_summary_
        just return a value of property class.

        Returns:
            str: value from object_line have a name of country.
        """
        return self.__name_country
    @property
    def currency_code(self) -> str:
        """_summary_
        just return a value of property class.

        Returns:
            str: value from object_line have a code of currency .
        """
        return self.__currency_code
    @property
    def rate(self) -> float:
        """_summary_
        just return a value of property class.

        Returns:
            float: value from object_line have a rate .
        """
        return self.__rate
    @rate.setter
    def rate(self,new_rate:float):
        """
        Sets a new exchange rate for the currency.

        Args:
            new_rate (float): The new rate value to be assigned.

        Raises:
            ValueError: If the value is not numeric or is negative.
        """
        try:
            new_rate=float(new_rate)
        except(TypeError,ValueError):
            raise ValueError("new_rate must be a numeric value")
        if new_rate < 0:
            raise ValueError("Rate cannot be negative.")
        self.__rate=new_rate
        if self.__mode==Currency.__c_mode.c_update:
            self.__update()
    def is_empty(self) -> bool:
        """
        validation if the object is empty.

        Returns:
            bool: if the object is empty return true otherwise false.
        """
        return(self.__mode==Currency.__c_mode.c_empty)  
    @staticmethod
    def __convert_line_to_obj(object_line_line,seperator="#//#"):
        """
        covvert linet in data base to object. 

        Args:
            object_line_line (Currency object): object from this class
            seperator (str, optional): to seperator bwteen propertice. Defaults to "#//#".

        Returns:
            object type: oject form type his class
        """
        country_data=object_line_line.split(seperator)
        return Currency(
            country_data[0],
            country_data[1],
            country_data[2],
            float(country_data[3]),
            Currency.__c_mode.c_update) 
    @staticmethod
    def __convert_obj_to_line(object_line,seperator="#//#"):  
        """
            covvert object in data base to line. 
        Args:
            object_line (currency object): write in data base.
            seperator (str, optional): to seperator bwteen propertice. Defaults to "#//#".

        Returns:
            string: for writting file.
        """
        line=str()
        line+=object_line.name_country+seperator
        line+=object_line.currency_code+seperator 
        line+=object_line.currency_name+seperator
        line+=str(object_line.rate)+seperator
        return line
    @staticmethod
    def __load_data_from_file():
        """
        Take a data from file put in list.

        Returns:
            list: list of object currencies.
        """
        list_data=list()
        path=Currency.__path_file()
        with open(path,"r") as file:
            for line in file:
                line=line.strip()
                line=Currency.__convert_line_to_obj(line)
                if line:
                    list_data.append(line)
        return list_data  
    @staticmethod
    def __get_empyt_object():
        """
        This is methode jsut leads to object ..
        Returns:
            empty obect : if you have a obect empty using this methodes
        """
        return Currency("","","",0.0,Currency.__c_mode.c_empty)      
    @staticmethod
    def find_by_country_name(name_contry:str):
        """
        To find a data have same name
        Args:
            name_contry (str): pass a name country to search a data for this name.

        Returns:
            obejct: all data same name pass it.
        """
        path=Currency.__path_file()
        list_obj=Currency.__load_data_from_file()
        for obj_name in list_obj:
            if obj_name.name_country.strip().lower() == name_contry.strip().lower():
                return obj_name
                    
        return Currency.__get_empyt_object()
    @staticmethod
    def find_by_country_code(currency_code:str):
        """
            To find a data have same currency code.
        Args:
            name_code(str): pass a currency code to search a data for this code.

        Returns:
            obect : all data same code pass it.
        """
        path=Currency.__path_file()
        list_obj=Currency.__load_data_from_file()
        for obj_code in list_obj:
            if obj_code.currency_code.strip().lower() == currency_code.strip().lower():
                return obj_code
                    
        return Currency.__get_empyt_object()
    @staticmethod
    def is_exist(input_value: str) -> bool:
        """
        Check if the given input_value exists as a country name or currency code.

        Args:
            input_value (str): country name or currency code.

        Returns:
            bool: True if exists, False otherwise.
        """
        if len(input_value) <= 3:
            country = Currency.find_by_country_code(input_value)
        else:
            country = Currency.find_by_country_name(input_value)

        return not country.is_empty()

    @staticmethod
    def __save_currency_to_file(currency_line):
        """
        Save new data in data base.
        Args:
            currency_line (string): new data put in data base.
        """
        path=Currency.__path_file()
        with open(path,"a") as file:
            line=Currency.__convert_obj_to_line(currency_line)
            file.write(line+"\n")
    def __update(self):
        """_summary_
        Just update rate.
        """
        list_currncey=Currency.__load_data_from_file()
        path=Currency.__path_file()
        update_state=False        
        for index, currency in enumerate(list_currncey):
            if currency.currency_code==self.currency_code:
                list_currncey[index]=self
                update_state=True 
                break
        if update_state:
            with open(path,"w")  as file:
                for currency in list_currncey:
                    line=Currency.__convert_obj_to_line(currency)
                    file.write(line+"\n")  
        else:
            Currency.__save_currency_to_file(self)   
    @staticmethod
    def get_currency_list():
        """
        To show currancies data.

        Returns:
            list of object: all data in data base as object.
        """
        return Currency.__load_data_from_file()     

