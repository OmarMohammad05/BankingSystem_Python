import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.clsPerson import clsPerson
from enum import Enum
class BankClient(clsPerson):
    __DATA_DIR="data"
    __FILE_NAME="Clients.txt"
    class SaveResult(Enum):
        svFailedEmptyObject =0
        svSucceeded=1
        svFailedNumberExists=2
        
    class Mode(Enum):
        EmptyMode = 0
        UpdateMode = 1 
        addNewMode=2
   
    def __init__(self,FirstName,LastName,Email,Phone,NewAccountNumber, NewPinCode, NewAccountBalance,NewMode ):
        super().__init__(FirstName, LastName, Email, Phone)
        self._AccountNumber=NewAccountNumber
        self._PinCode=NewPinCode
        self._AccountBalance=NewAccountBalance
        self._Mode=NewMode 
    def IsEmpty(self):
        return self._Mode==BankClient.Mode.EmptyMode  
         
    @property
    def AccountNumber(self):
        return self._AccountNumber
    @property
    def PinCode(self):
        return self._PinCode
    @PinCode.setter
    def PinCode(self, NewPinCode):
        self._PinCode=NewPinCode
    @property
    def AccountBalance(self):
        return float(self._AccountBalance)
    @AccountBalance.setter
    def AccountBalance(self, NewAccountBalance:float):
        self._AccountBalance=NewAccountBalance  
         
    def Deposit(self, amount:float):
        self.AccountBalance+=amount
        self.Save()
    def Withdraw(self ,amount:float):
        if self.AccountBalance>=amount:
            self.AccountBalance-=amount
            self.Save()
            return True
        return False

    @staticmethod
    def _ConvertLineToClientObject(line , separator="#//#"):
        """_summary_

        Args:
            line data
            separator (str, optional): _description_. Defaults to "#//#".

        Returns:
            object class: _description_
        """
        vClientData=line.split(separator)
        return BankClient(
            vClientData[0],  # FirstName
            vClientData[1],  # LastName
            vClientData[2],  # Email
            vClientData[3],  # Phone
            vClientData[4],  # AccountNumber
            vClientData[5],  # PinCode
            vClientData[6],  # AccountBalance
            BankClient.Mode.UpdateMode  # Mode 
            
        )   
    @staticmethod
    def GetEmptyClientObject():
        return BankClient("","","","","","",0, BankClient.Mode.EmptyMode)     
    @staticmethod
    def __path():
        path=os.path.join(BankClient.__DATA_DIR,BankClient.__FILE_NAME)
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found {path} ")
        return path
    @staticmethod
    def _LoadClientFromFile():
        clients=list()
        with open(BankClient.__path(),'r') as file:
            for line in file:
                line=line.strip()
                client=BankClient._ConvertLineToClientObject(line)
                clients.append(client)
        return clients    
    @staticmethod
    def _ConvertClientObjectToLine(client , separator="#//#"):  
        stClient=str()
        stClient+=client.FirstName+separator
        stClient+=client.LastName+separator
        stClient+=client.Email+separator
        stClient+=str(client.Phone)+separator
        stClient+=str(client.AccountNumber)+separator
        stClient+=str(client.PinCode)+separator
        stClient+=str(client.AccountBalance)
        return stClient
    
    @staticmethod
    def Find(account_number, pin_code=None):
        with open(BankClient.__path()) as file:
            for line in file:
                client=BankClient._ConvertLineToClientObject(line)
                if pin_code is None:
                    if client.AccountNumber==account_number:
                        return client
                else:
                    if client.AccountNumber==account_number and client.PinCode==pin_code:
                        return client
                    
            return BankClient.GetEmptyClientObject()  
    @staticmethod
    def IsClientExist(account_number):
        client=BankClient.Find(account_number)
        return not client.IsEmpty()  
    @staticmethod
    def _SaveClientDataToFile(client):
        with open(BankClient.__path(),'a') as file:
                line=BankClient._ConvertClientObjectToLine(client)
                file.write(line+"\n")
                
    def _Update(self):
        ListClients=BankClient._LoadClientFromFile()
        for i,client in enumerate(ListClients):
            if client.AccountNumber == self.AccountNumber:
                ListClients[i]=self
                break
        with open(BankClient.__path(), "w") as file:
            for c in ListClients:
                line = BankClient._ConvertClientObjectToLine(c)
                file.write(line + "\n")  
    @staticmethod   
    def GetAddNewClientObject(accountNumber):
        return BankClient("","","","",accountNumber,"",0,BankClient.Mode.addNewMode)            
    @staticmethod            
    def __AddDataToFile(dataLine):
     """
     Save client data to file without overwriting existing data.
     """
     with open(BankClient.__path(),'a') as file:
         file.write(dataLine+"\n")            
    def __AddNew(self):
        BankClient.__AddDataToFile(self._ConvertClientObjectToLine(self)) 
        
    def Save(self):
        if self._Mode ==self.Mode.EmptyMode:
            return self.SaveResult .svFaildEmptyObject   
        elif self._Mode == self.Mode.UpdateMode:
            self._Update()    
            return self.SaveResult.svSucceeded    
        elif self._Mode==self.Mode.addNewMode:
            if BankClient.IsClientExist(self._AccountNumber):
                return self.SaveResult.svFailedNumberExists
            else:
                self.__AddNew()
                self.Mode=self.Mode.UpdateMode
                return self.SaveResult.svSucceeded
   
    def delete(self):
        """
          This`s methode for delete client .
          to search on the account number and dont append on the file.
        
        """
        clientObject=list()
        clientObject=BankClient._LoadClientFromFile() # Load data from file.
        #Save data in varible.
        # self.AccountNumber this is value of current client(Object)
        # client.AccountNumber this is value from loop in list object.
        
        newClients=[client for client in clientObject if client.AccountNumber != self.AccountNumber]
        with open(BankClient.__path(), "w") as file:
            for line in newClients:
                clientLine=BankClient._ConvertClientObjectToLine(line)
                file.write(clientLine+"\n")
           
        return BankClient.GetEmptyClientObject()  
    @staticmethod
    def GetListClient():
        return BankClient._LoadClientFromFile()     
    @staticmethod
    def GetTotalBalance():
        clients=BankClient.GetListClient()  
        totalBalance=0.0
        for client in clients:
            totalBalance+=client.AccountBalance
        return totalBalance
                      

                           
