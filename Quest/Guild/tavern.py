from Class.fighter import Fighter
from random import randint
from Quest.Guild.generateNPC import generateNPC


def Recruit(playerClass, party):
    """handles all ai party recruitment"""
    print("\nYou have entered the Guild tavern! \n")
    recruits = randint(2, 5)
    print("There are "+str(recruits)+" men and women in the tavern waiting to find work. ")
    print("Entering the tavern, you leave 30 gold coins on the counter to reserve an area.")
    print("Sitting down on a stained stool, you wait for potential members to approach you.")
    playerClass.gold += -30

    for person in range(recruits):
        if len(party) < 3:
            ai = generateNPC(playerClass)
            cost = 10 * ai.level + randint(1, 5) * 5
            print("\nWill you hire "+ai.name+" the "+ai.classType+" for "+str(cost)+" gold pieces? [y/n]")
            valid = False
            while valid == False:
                hire = input()
                if hire == 'y':
                    print("You have hired "+ai.name+" for "+str(cost)+" gold.\n")
                    party.append(ai)
                    playerClass.gold += -cost
                    valid = True
                elif hire == 'n':
                    print("You motion to the next candidate.\n")
                    valid = True
                else:
                    print("Invalid Input")
        else:
            print("Currently at max party size.")
            break
    print("\nYour current party is:\n")
    for member in party:
        print(member.name+", class: "+member.classType+", level:"+str(member.level))
    print("\nWith your current party, you return to the main hall.\n")

if __name__ == "__main__":
    playerClass = Fighter("Ted", 1, 5, 5, 10, 5, 6, 2, 9)
    playerClass.initPlayer(1)
    party = []
    party.append(playerClass)
    Recruit(playerClass, party)
