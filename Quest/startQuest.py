


def startQuest(playerClass, party, Quest):
    for member in party:
        member.hp = member.maxHp
        member.damage = member.baseDmg
        member.armour = member.baseArmour
        member.contribution = 0
        member.threat = 0
        member.action = None
        member.target = None
        if member.classType == "mage":
            member.mana = 10
        if member.classType == "cleric":
            member.doubt = 0
