from random import randint
from random import choice


class Base:
    """Base traits and stats for all character classes"""

    def __init__(self, name, level, maxHp, morale, dmg, armour):
        self.enemy = True
        self.name = name
        self.level = level
        self.loot = 0
        # Class specific
        self.maxHp = maxHp
        self.hp = maxHp
        self.morale = morale
        self.baseDmg = dmg
        self.armour = armour
        # Combat Values
        self.threat = 0
        self.distance = 3
        self.action = None
        self.target = None
        self.damage= self.baseDmg

    def calculateAction(self, enemy, party):
        """Performs roll for AI calculateAction. To be overwritten in each class."""
        """Performs roll for AI calculateAction."""
        target = choice(enemy)
        self.target = target

    def updateHp(self, damage):
        """Input the amount of damage dealt."""
        if self.armour < 0:
            self.armour = 0
        if damage < 0:
            print(self.name + " was healed for " + str(-damage) + ".")
        elif damage > self.armour:
            print(self.name+" was damaged for "+str(damage)+".")
            self.hp += -damage
            self.morale += -damage
        else:
            print("The blow bounced off "+self.name+"'s armour!")
        if self.hp > self.maxHp:
            self.morale = self.hp - self.maxHp
            self.hp = self.maxHp
        print(str(self.hp)+" hp left!")

    def death(self, party):
        print(self.name+" has been slain!")
        party.remove(self)

    def partyDeath(self, target, party):
        print(self.name + "has killed " + target.name + "!")
        party.remove(target)