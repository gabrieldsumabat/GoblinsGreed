from Class.fighter import Fighter
from Class.ranger import Ranger
from Class.cleric import Cleric
from Class.mage import Mage
from random import randint

def generateNPC(level):
    classSelect = randint(1,4)
    names = ()

    if classSelect == 1:
        NPC = Fighter()
    elif classSelect == 2:
        NPC = Ranger()
    elif classSelect == 3:
        NPC = Cleric()
    else:
        NPC = Mage()
    return NPC



if __name__ == "__main__":
    generateNPC(1)