import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from enum import IntEnum
from core.clsPerson import clsPerson
import json
from datetime import datetime
from core.SecurityPasswrod import Security
class User(clsPerson):
    __DATA_DIR="data"
    __FILE_NAME="User.txt"
    class enPermission(IntEnum):
        eAll=-1
        pListClient=1
        pAddNewClinet=2
        pDeleteClinet=4
        pUpdateClinet=8
        pFindClinet=16
        pTransactionClient=32
        pManageUsers=64
        pShowRigesterUser=128
    class _eMode(IntEnum):
        eEmptyMode=0
        eUpdateMode=1
        eAddNewMode=2
    class enSave(IntEnum):
        svFaildEmptyObject=0
        svSuccesed=1  
        svUserExists=2
    def __init__(self,FirstName,LastName,Email,Phone, NewUserName, NewPassword, NewPermissions:int,mode):
        super().__init__(FirstName, LastName, Email, Phone)   
        self.__UserName=NewUserName
        self.__Password=NewPassword
        self.__Permissions=NewPermissions
        self.__Mode=mode
    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self,newUserName):
        self.__UserName=newUserName
    
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self,newPass):
        self.__Password=newPass
        
    @property
    def Permissions(self):
        return self.__Permissions    
    @Permissions.setter
    def Permissions(self,newPermission:int):
        self.__Permissions=newPermission 
        
    def IsEmpty(self):
        return  self.__Mode == User._eMode.eEmptyMode     
    @staticmethod
    def __GetEmptyObject():
        return User("","","","","","",0,User._eMode.eEmptyMode)  
    @staticmethod
    def __Path():
        """_summary_
        
        This methode jsut take a path of file.

        Raises:
            FileNotFoundError: file not fount.

        Returns:
            _type_: path of data base.
        """
        path=os.path.join(User.__DATA_DIR,User.__FILE_NAME)
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found {path} ")
        return path
             
    @staticmethod
    def __ConvertLineToUserObject(user,seperator="#//#"):
        userData=user.split(seperator)
        return User(
            userData[0],
            userData[1],
            userData[2],
            userData[3],
            userData[4],
            Security.Decryp(userData[5]),
            int(userData[6]),
            User._eMode.eUpdateMode)
    @staticmethod
    def __ConvertObjectToLine(user,seperator="#//#"):
        user_record=str()
        user_record+=user.FirstName+seperator
        user_record+=user.LastName+seperator
        user_record+=user.Email+seperator
        user_record+=str(user.Phone)+seperator
        user_record+=user.UserName+seperator
        user_record+=Security.Encryp(user.Password)+seperator
        user_record+=str(user.Permissions)
        return user_record
    @staticmethod
    def __LoadUserFromFile():
         users=list()
         with open(User.__Path(),"r") as file:
             for line in file:
                 line=line.strip()
                 user=User.__ConvertLineToUserObject(line)
                 users.append(user) 
         return users  
    @staticmethod
    def __SaveUserToFile(user):
        with open(User.__Path(),"a") as file:
            line=User.__ConvertObjectToLine(user)
            file.write(line+"\n")
    def __Update(self):
        listUser=User.__LoadUserFromFile()
        updated=False
        for i ,user in enumerate(listUser):
            if user.UserName==self.UserName:
                listUser[i]=self
                updated=True
                break
                
        if updated:        
            with open(User.__Path(),"w") as file:
                for user in listUser:
                    line=User.__ConvertObjectToLine(user)
                    file.write(line+"\n")
        else:
            User.__SaveUserToFile(self)   
            
    @staticmethod         
    def __AddDataToFile(user):
        with open(User.__Path(),"a") as file:
            file.write(user+"\n")
    def __AddNewUser(self):
        User.__AddDataToFile(User.__ConvertObjectToLine(self)) 
        
    @staticmethod    
    def Find(userName,password=None):
        listUser=User.__LoadUserFromFile()
        for user in listUser:
            if password is None:
                if user.UserName == userName:
                    return user
            else:
                if user.UserName==userName and user.Password == password:
                    return user          
        return User.__GetEmptyObject()     
    @staticmethod
    def IsUserExist(userName):
        user=User.Find(userName)
        return not user.IsEmpty()
     
    def Save(self):
        if self.__Mode == self._eMode.eEmptyMode:
            return self.enSave.svFaildEmptyObject
        elif self.__Mode == self._eMode.eUpdateMode:
            self.__Update()
            return self.enSave.svSuccesed
        elif self.__Mode == self._eMode.eAddNewMode:
            if User.IsUserExist(self.__UserName):
                return self.enSave.svUserExists
            else:
                self.__AddNewUser()
                self.__Mode=self._eMode.eUpdateMode
                return self.enSave.svSuccesed
    @staticmethod
    def GetAddNewUserObject(userName):
        return User("","","","",userName,"",0,User._eMode.eAddNewMode)
    @staticmethod
    def GetUsersList():
        return User.__LoadUserFromFile()
    
    def Delete(self):
        allUser=User.__LoadUserFromFile()
        newUsers=[user for user in allUser if user.UserName != self.UserName]    
        with open(User.__Path(),"w") as file:
            for line in newUsers:
                user=User.__ConvertObjectToLine(line)
                file.write(user+"\n")    
        return User.__GetEmptyObject()       
    def CheckAccessPermission(self,permission:enPermission ):
        if self.__Permissions ==User.enPermission.eAll:
            return True
        if (permission & self.__Permissions) == permission:
            return True
        else:
            return False
    
    def __DataFormat(self):
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data={
            "UserName":self.UserName,
            "FirstName":self.FirstName,
            "LastName":self.LastName,
            "Premissions":self.Permissions,
            "Date":date_str
        }
        return data    
    @staticmethod
    def __pathOfJsonLogIn():
        return os.path.join("data","logFile.json")
    def RegisterLogIn(self):
        path=User.__pathOfJsonLogIn()
        data=self.__DataFormat()  
        if os.path.exists(path):
            with open(path,"r") as file:
                try:
                    # load all data from json file because append new object in list json..
                    all_data=json.load(file)
                    # To check(Data type) the data is dict or not if is dict converted to list..
                    if isinstance(all_data,dict):
                        all_data=[all_data]
                # if the json file is not corrected and I wannt not stoped function ....     
                except json.JSONDecodeError:
                    all_data=[]
        # no file all data list is empty..            
        else:
            all_data=[]
        # add new data in the list...    
        all_data.append(data) 
        #open json file in the write mode to write all data with new data(instance) put in json file.
        with open(path,"w") as f:
            # the wirtie data .....
            json.dump(all_data,f, indent=4)  
    @staticmethod
    def ListOfLogInRegister():
        data=list() 
        path=User.__pathOfJsonLogIn()
        if not  os.path.exists(path):
           return "The path is not correct"
        with open(path,"r") as file:
            try:
               data=json.load(file)
            except json.JSONDecodeError:
                   return "The json is not correct"
        return data       
                  


