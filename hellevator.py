from __future__ import absolute_import
from lib2to3.pgen2.tokenize import StopTokenizing

from sqlalchemy import true


soption = int(input("Satan, what floor?: "))

foption = int(input("Friend, what floor do you choose?: "))

def hellmath(foption, soption):
    if foption == soption:
        print("rule 1")
        return True
    elif foption > 80:
        print("rule 2")
        return True
    elif foption < (666-80):
        print("rule 3")
        return True
    elif abs(foption - soption) < 161:
        print("rule 4")
        return True
    elif foption == 365:
        print("rule 5")
        return True
    else: 
        return False

def hellevator(foption, soption,):
    if hellmath(foption, soption) ==  False :
        print("welcome to heaven!")
    else:
        print("you will die")

print(hellevator(foption, soption))