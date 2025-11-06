import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from core.clcUser import User

current_user=User.Find("","")