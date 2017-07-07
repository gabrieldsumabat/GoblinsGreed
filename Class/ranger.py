import Class.base
from random import randint
from random import choice


class Ranger(Class.base.Base):
    """Base Ranger Class"""
    def __init__(self, name, level, alignment, trust, maxHp, morale, dmg, armour, greed):
        super().__init__(name, level, alignment, trust, maxHp,  morale, dmg, armour, greed)
        # Need to modify these values to scale with their level later
        self.classType = "ranger"

    def steelShot(self, target, party):
        """An armour damaging strike, due to its strength you might miss and hit an ally!"""
        self.action = "steelShot"
        print(self.name+" readies a powerful steel arrow!")
        if randint(1, 4) == 4:
            inRange = []
            for hero in party:
                if hero.name != self.name:
                    inRange.append(hero)
            if len(inRange) != 0:
                target = choice(inRange)
                print("Its a disaster!"+target.name+" has just been hit by "+self.name+"'s steel arrow!!")
                target.armour = target.armour - randint(1, 3)
                target.updateHp(self.damage)
                self.target = target
            else:
                print(self.name+"'s arrow missed completely!")
        else:
            print("The steel arrow strikes "+target.name+" and damages their armour!")
            target.armour = target.armour - randint(1, 3)
            target.updateHp(self.damage)
            self.target = target

    def quickShot(self, target):
        """A fast accurate shot at the unarmoured spots on the enemy."""
        self.action = "quickShot"
        self.target = target
        print(self.name+" prepares a small arrow.")
        target.updateHp(self.damage*2)

    def stab(self, target):
        """Stabs the enemy, ignores armour"""
        self.action = "stab"
        self.target = target
        if target.armour < 0:
            print(self.name+" stabs "+target.name+" unprotected flesh!")
            target.updateHp(self.damage)
        else:
            print(self.name+" stabs through "+target.name+"'s armour!")
            target.updateHp(self.damage+target.armour)

    def bullseye(self):
        """Increases damage in this battle."""
        self.action = "bullseye"
        print(self.name+" studies the enemy slowly.")
        self.damage = self.damage+5
        print(self.name+" has increased their damage by five!")
