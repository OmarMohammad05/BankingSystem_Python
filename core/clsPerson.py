class clsPerson:
    #------------Constructor--------------
    def __init__(self, NewFirstName , NewLastName , NewEmail , NewPhone):
        # Not the data member is begining of __ ,but the any object started New this is new value should by pass when u create object from class.
        self.__FirstName=NewFirstName 
        self.__LastName=NewLastName
        self.__Email=NewEmail
        self.__Phone=NewPhone
    #--------------First name -------------------    
    @property # To read data
    def FirstName(self):
        """"
        This`s function to get 1st name
        
        """""
        return self.__FirstName
    @FirstName.setter # To edit data
    def FirstName(self,newFname):
        """"
        This`s function to set 1st name
        
        """""
        self.__FirstName=newFname
    #--------------Last name -------------------    
    @property
    def LastName(self):
        """"
        This`s function to get last name
        
        """""
        return self.__LastName    
    @LastName.setter
    def LastName(self,newLname):
        """"
        This`s function to set last name
        
        """""
        self.__LastName=newLname
    #--------------Email -------------------    
    @property
    def Email(self): 
        """"
        This`s function to get email
        
        """""
        return self.__Email
    @Email.setter
    def Email(self,newEmail):
        """"
        This`s function to set email
        
        """""
        self.__Email=newEmail
    #--------------Phone -------------------
    @property
    def Phone(self):
        """"
        This`s function to get phone
        
        """""
        return self.__Phone
    @Phone.setter
    def Phone(self,newPhone):
        """"
        This`s function to set phone
        
        """""
        self.__Phone=newPhone     
    #--------------Full name -------------------   
    def FullName(self):
        return f"{self.__FirstName} {self.__LastName}"



    
