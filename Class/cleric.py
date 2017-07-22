import Class.base
from random import randint


class Cleric(Class.base.Base):
    """Base Cleric Class"""
    def __init__(self, name, level, alignment, trust, maxHp, morale, dmg, armour, greed):
        super().__init__(name, level, alignment, trust, maxHp,  morale, dmg, armour, greed)
        # Need to modify these values to scale with their level later
        self.doubt = 0
        self.classType = "cleric"

    def zeal(self, target):
        """The cleric tests his targets faith!"""
        self.action = "zeal"
        self.target = target
        if randint(1, 3) == 3:
            print(target.name+"'s faith was found wanting! "+self.name+" smites the heretic!")
            target.updateHp(self.damage)
            self.trust += -self.damage
            self.morale += -self.damage
            self.threat += -self.damage
            self.contribution += -self.damage
        else:
            print(target.name+" has received a blessing!")
            target.updateHp(-self.damage)
            print(target.name+" has increased their damage by five!")
            target.damage = target.damage+5
            self.trust += self.damage
            self.morale += self.damage
            self.threat += self.damage
            self.contribution += self.damage

    def heal(self, target):
        """The cleric heals the wounded."""
        self.action = "heal"
        self.target = target
        print(self.name+" has healed "+target.name+"!")
        target.updateHp(-self.damage//2)
        self.trust += self.damage
        self.morale += self.damage
        self.threat += self.damage
        self.contribution += self.damage

    def martyr(self):
        """The cleric stands tall as an icon!"""
        self.action = "martyr"
        print(self.name+"'s courage impresses the party!")
        self.trust += self.damage
        self.morale += self.damage
        self.threat += self.damage * 2

    def pray(self):
        """The cleric prays to his deity."""
        self.action = "pray"
        print(self.name+" prays to his deity for strength.")
        if randint(1, 4) == 4:
            print(self.name+" was found wanting! His doubt grows...")
            self.doubt += 5
            print(self.name+" grows concerned with his path...")
            self.damage += -5
            self.morale += -5
        else:
            self.doubt += -self.damage * 2

