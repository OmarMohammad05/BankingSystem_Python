class ReadClientInfo:
    @staticmethod
    def ReadClient(client):
        """_summary_
        This is function to input new information for one client

        Args:
        client (object clcBank): 
        
        """
        fileds={
            "first name":"FirstName",
            "last name": "LastName",
            "email":"Email",
            "phone":"Phone",
            "pin code":"PinCode",
            "account balance":"AccountBalance"
        } 
        while True:
            choose=input("\nEnter the field you want to update (all/exit):").lower()
            if choose == "exit":
                break
            elif choose == "all":
                for filed , att in fileds.items():
                    value=input(f"\n Enter {filed}: ")
                    if filed == "account balance":
                        value=float(value)
                    setattr(client , att , value) 
            elif choose in fileds:
                value=input(f"\n Enter {choose}: ")   
                if choose == "account balance":
                    value=float(value)
                setattr(client, fileds[choose] , value)   # for  assinge value to object 
            else:
                print("Invalid choice, try again.")
              