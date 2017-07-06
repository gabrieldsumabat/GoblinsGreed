from Class.fighter import Fighter
from Class.ranger import Ranger
from Class.cleric import Cleric
from Class.mage import Mage
from random import randint
from random import choice


def generateNPC(playerClass):
    """generates ai players"""
    classSelect = randint(1, 4)
    if playerClass.level > 1:
        level = playerClass.level - randint(-1, 1)
    else:
        level = playerClass.level
#   name, level, alignment, trust, maxHp, morale, dmg, armour, greed
    if classSelect == 1:
        names = ["Tyr", "Myke", "Terd"]
        name = choice(names)
        alignment = level * randint(1, 2)
        trust = randint(3, 10)
        maxHp = level * randint(1, 2) + 10
        morale = playerClass.reputation + randint(1, 2)
        dmg = level * randint(1, 2) + 10
        armour = level * randint(1, 2) + 10
        greed = randint(1, 2) - morale
        NPC = Fighter(name, level, alignment, trust, maxHp, morale, dmg, armour, greed)
    elif classSelect == 2:
        names = ["Tyr", "Myke", "Terd"]
        name = choice(names)
        alignment = level * randint(1, 2)
        trust = randint(3, 10)
        maxHp = level * randint(1, 2) + 10
        morale = playerClass.reputation + randint(1, 2)
        dmg = level * randint(1, 2) + 10
        armour = level * randint(1, 2) + 10
        greed = randint(1, 2) - morale
        NPC = Ranger(name, level, alignment, trust, maxHp, morale, dmg, armour, greed)
    elif classSelect == 3:
        names = ["Tyr", "Myke", "Terd"]
        name = choice(names)
        alignment = level * randint(1, 2)
        trust = randint(3, 10)
        maxHp = level * randint(1, 2) + 10
        morale = playerClass.reputation + randint(1, 2)
        dmg = level * randint(1, 2) + 10
        armour = level * randint(1, 2) + 10
        greed = randint(1, 2) - morale
        NPC = Cleric(name, level, alignment, trust, maxHp, morale, dmg, armour, greed)
    else:
        names = ["Tyr", "Myke", "Terd"]
        name = choice(names)
        alignment = level * randint(1, 2)
        trust = randint(3, 10)
        maxHp = level * randint(1, 2) + 10
        morale = playerClass.reputation + randint(1, 2)
        dmg = level * randint(1, 2) + 10
        armour = level * randint(1, 2) + 10
        greed = randint(1, 2) - morale
        NPC = Mage(name, level, alignment, trust, maxHp, morale, dmg, armour, greed)
    return NPC


