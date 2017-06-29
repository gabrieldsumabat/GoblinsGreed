from Class.fighter import Fighter
from Class.ranger import Ranger
from Class.cleric import Cleric
from Class.mage import Mage
from random import randint

def Recruit(party):
    print("""
    You have entered the Guild tavern!
    You can recruit potential allies to fill your party here. 
    Remember that you have a maximum party size of three!""")

    recruits = randint(2, 7)

if __name__ == "__main__":
    playerClass = Fighter("Ted", 1, 5, 5, 10, 5, 6, 2, 9)
    party = []
    Recruit(party)
