from Quest.Guild import guild


class Quest:
    """base quest traits"""

    def __init__(self, name, level, description, bounty, boss, area):
        self.name = name
        self.description = description
        self.level = level
        self.bounty = bounty
        self.boss = boss
        self.area = area

    def success(self, playerClass, party):
        playerClass.gold += self.bounty
        playerClass.reputation += self.level
        for member in party:
            member.morale += self.level

    def failure(self, playerClass, party):
        playerClass.reputation += -self.level

    def returnGuild(self, playerClass, party):
        guild(playerClass, party)

    def startQuest(self, playerClass, party):
        for member in party:
            member.hp = member.maxHp
            member.damage = member.baseDmg
            member.armour = member.baseArmour
            member.contribution = 0
            member.threat = 0
            member.calculateAction = None
            member.target = None
            if member.classType == "mage":
                member.mana = 10
            if member.classType == "cleric":
                member.doubt = 0




