class Quest:
    """base quest traits"""

    def __init__(self, name, level, description, bounty, boss):
        self.name = name
        self.description = description
        self.level = level
        self.bounty = bounty
        self.boss = boss

    def success(self, playerClass, party):
        playerClass.gold += self.bounty
        playerClass.reputation += self.level
        for member in party:
            member.morale += self.level

    def failure(self, playerClass, party):
        playerClass.reputation += -self.level



