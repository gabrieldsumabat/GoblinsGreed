import Class.base
from random import randint
from random import choice


class Fighter(Class.base.Base):
    """Base Fighter Class"""
    def __init__(self, name, level, alignment, trust, maxHp, morale, dmg, armour, greed):
        super().__init__(name, level, alignment, trust, maxHp,  morale, dmg, armour, greed)
        # Need to modify these values to scale with their level later
        self.classType = "fighter"

    def cleave(self, target, party):
        """A wide swing intended for maximum effect. May hit allies."""
        self.action = "cleave"
        self.target = target
        print(self.name+" swings a mighty strike at the enemy!")
        if randint(1, 3) == 3:
            print("A disaster! "+self.name+" has hit an ally with his great strike!")
            inRange = []
            for hero in party:
                if hero.name != self.name:
                    inRange.append(hero)
            if len(inRange) != 0:
                target = choice(party)
                self.target = target
                print(target.name+" has just been hit by "+self.name+"'s great cleave!")
                target.updateHp(self.damage * 3)
                self.morale += -self.damage * 3
                self.contribution += -self.damage*2
                self.threat = -self.damage
                self.trust += -self.damage * 3
            else:
                print(self.name+"'s strike missed completely!")
                self.contribution += -self.damage
                self.trust += -self.damage
                self.morale += -self.damage
        else:
            print(self.name+" has landed a mighty blow on the enemy!")
            target.updateHp(self.damage * 3)
            self.morale += self.damage * 3
            self.contribution += self.damage * 3
            self.threat = self.damage * 3
            self.trust += self.damage

    def slash(self, target):
        """A heavy blow to their midsection."""
        self.action = "slash"
        self.target = target
        print(self.name+" slashes "+target.name)
        target.updateHp(self.damage)
        self.morale += self.damage
        self.threat += self.damage
        self.contribution += self.damage//2
        self.trust += self.damage // 2

    def charge(self, target, party):
        """Close the distance!"""
        self.action = "charge"
        self.target = target
        print(self.name+" charges the enemy!")
        target.updateHp(self.damage//2)
        print(self.name+" stabs the enemy with the point of the blade and inspires the party!")
        for member in party:
            member.morale += self.damage//2
        self.contribution += self.damage
        self.threat += self.damage * 2
        self.trust += self.damage // 2

    def blunt(self, target):
        """Swings a blunt strike which damages the targets armour"""
        self.action = "blunt"
        self.target = target
        if self.damage <= 5:
            rend = 2
        else:
            rend = self.damage//3
        print(self.name+" swings a blunted strike at "+target.name+"'s armour!")
        target.armour += -randint(1, rend)
        print(target.name+"'s armour has been damaged!")
        self.contribution += rend
        self.threat += rend*3
        self.trust += rend


