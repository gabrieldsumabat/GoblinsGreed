from Monsters.base import Base
from random import randint


class BanditWolf(Base):

    def __init__(self, name, level, maxHp, hp, morale, dmg, armour):
        super().__init__(name, level, maxHp, hp, morale, dmg, armour)
        self.moon = False
        self.transform = False

    def fullmoon(self):
        """When wounded under a full moon, transform into a werewolf"""
        self.action = "fullmoon"
        if self.transform == False:
            print(self.name+" lets out a terrifying howl! His body grows a layer of hair and a pair of sharp claws!")
            self.transform = True
            self.damage += 2*self.level
            self.armour += self.level
            self.hp += randint(1, 2) * self.level
            print(self.name+" gains increased damage and armour. He will regenerate hp each turn!")
        else:
            print(self.name+" regenerates in front of your eyes!")
            self.hp += randint(1, 2 * self.level)

    def slash(self, target):
        """slashes a party member"""
        self.action = "slash"
        print(self.name+" slashes "+target.name+"!")
        target.updateHP(self.damage)

    def bash(self, target):
        """bashes the enemy whis his shield or first"""
        self.action = "bash"
        if self.transform:
            print(self.name+" slams his fist into "+target.name+".")
            target.updateHP(self.damage//2)
            target.morale += -4
        else:
            print(self.name + " slams his shield into "+target.name+".")
            target.updateHP(self.damage // 2)
            target.morale += -2

    def rend(self, target):
        """tears at the target's armour"""
        self.action = "rend"
        if self.transform:
            print(self.name+" uses his claws to rend "+target.name+"'s armour.")
            target.updateHP(self.damage//2)
            target.armour += -self.level*2
        else:
            print(self.name + " uses his axe to damage "+target.name+"'s armour.")
            target.updateHP(self.damage // 2)
            target.morale += -self.level

    def whirlwind(self, party):
        """a spinning attack which reduces his armour, but damages the entire party"""
        self.action = "whirlwind"
        print(self.name+" suddenly spins striking the entire party!")
        for member in party:
            if self.transform:
                member.updateHp(self.damage)
            else:
                member.updateHp(self.damage // 2)
                print("The attack has revealed weak spots in his armour!")
                self.armour += -self.level
