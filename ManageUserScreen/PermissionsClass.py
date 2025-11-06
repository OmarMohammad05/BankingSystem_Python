import os ,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from core.clcUser import User
class Permission:
    @staticmethod
    def Permissions():
        Permission=0
        dict_permission={"full access":User.enPermission.eAll,
                        "Show Client List":User.enPermission.pListClient,
                        "Add New Client":User.enPermission.pAddNewClinet,
                        "Delete Client":User.enPermission.pDeleteClinet,
                        "Update Client":User.enPermission.pUpdateClinet,
                        "Find Client":User.enPermission.pFindClinet,
                        "Transactions":User.enPermission.pTransactionClient,
                        "Manage Users":User.enPermission.pManageUsers,
                        "Show Rigester User": User.enPermission.pShowRigesterUser
                        }
        for key,value in dict_permission.items():
            choes=input(f"\nDo you want to give {key}? y/n?").lower()
            if choes=="y":
                Permission=Permission+value
                if key=="full access":
                    return Permission
            else:
                continue    
        return Permission    
