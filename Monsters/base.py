from random import randint


class Base:
    """Base traits and stats for all character classes"""

    def __init__(self, name, level, maxHp, hp, morale, dmg, armour):
        self.name = name
        self.level = level
        self.loot = 0
        # Class specific
        self.maxHp = maxHp
        self.hp = hp
        self.morale = morale
        self.baseDmg = dmg
        self.armour = armour
        # Combat Values
        self.threat = 0
        self.distance = 3
        self.action = None
        self.target = None
        self.damage= self.baseDmg

    def actionRoll(self, morale):
        """Performs roll for AI action."""
        return morale+randint(1, 6)*randint(1, 6)

    def updateHp(self, damage):
        """Input the amount of damage dealt."""
        print(self.name+" was damaged for "+str(damage))
        self.hp = self.hp - damage
        if self.hp > self.maxHp:
            self.hp = self.maxHp
        if self.hp <= 0:
            self.death()
        self.morale = self.morale-damage

    def death(self):
        print(self.name+" has been slain!")
