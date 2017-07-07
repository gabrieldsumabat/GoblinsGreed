import Class.base
from random import randint


class Mage(Class.base.Base):
    """Base Mage Class"""
    def __init__(self, name, level, alignment, trust, maxHp, morale, dmg, armour, greed):
        super().__init__(name, level, alignment, trust, maxHp,  morale, dmg, armour, greed)
        # Need to modify these values to scale with their level later
        self.mana = 10
        self.classType = "mage"

    def fireball(self, target, party):
        """A searing explosive ball of fire is unleashed!"""
        self.action = "fireball"
        self.target = target
        print(self.name+" gathers a burning ball of fire in his hands!")
        if randint(1, self.mana) < 5:
            print("Its a disaster!"+self.name+"'s fireball has just exploded in his own hands!")
            self.updateHp(self.damage * 2)
            for member in party:
                if member.name != self.name:
                    member.updateHp(self.damage)
                    if member.hp <= 0:
                        self.partyDeath(member, party)
        else:
            print("The fireball explodes on "+target.name+" and burns them alive!")
            target.updateHp(self.damage*5)
        self.mana = self.mana - randint(1, self.mana//2)

    def flameBolt(self, target):
        """A controlled flame bolt aimed at piercing the enemy armour"""
        self.action = "flameBolt"
        self.target = target
        print(self.name+" forms a spear of fire!")
        if randint(1, self.mana) < 2:
            print("The spell collapses and the flame bolt explodes!")
            self.updateHp(self.damage)
        else:
            if target.armour > 0:
                print("A searing bolt of fire strikes through " + target.name + " armour!")
                target.updateHp(self.damage+target.armour)
            else:
                print("A searing bolt of fire strikes " + target.name + "'s flesh!")
                target.updateHp(self.damage*2)

    def lifeleech(self, party):
        """The mage leeches his allies lifeforce to increase his mana"""
        self.action = "lifeleech"
        print("To power his arcane spell, "+self.name+" leeches the party's life force!")
        leech = len(party)
        for member in party:
            if member.name != self.name:
                if member.hp > 2:
                    member.hp += -2
                    print(member.name+"'s health decreased by two!")
                else:
                    leech += -1
                    print(member.name+" doesn't have enough lifeforce left!")

        print(self.name+"'s mana increases by "+str(leech*2)+"!")
        self.mana += leech*2

    def channel(self):
        """The mage channels his inner strength"""
        self.action = "channel"
        self.mana += randint(1, 2)
        print(self.name + " channels his concentration increasing his available mana to "+str(self.mana)+"!")

