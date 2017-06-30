from Class.fighter import Fighter
from random import randint
from Quest.Guild.generateNPC import generateNPC


def Recruit(playerClass, party):
    print("""
    You have entered the Guild tavern!
    You can recruit potential allies to fill your party here. 
    Remember that you have a maximum party size of three!""")

    recruits = randint(2, 7)

    print("There are "+str(recruits)+" men and women in the tavern waiting to find work. ")
    print("Sitting down on a stained stool, you motion them to cover over one at a time.")

    for person in range(recruits):
        ai = generateNPC(playerClass)
        cost = 10 * ai.level + randint(1, 5) * 5
        print("Will you hire "+ai.name+" the "+ai.classType+" for "+str(cost)+" gold pieces? [y/n]")
        valid = False
        while valid == False:
            hire = input()
            if hire == 'y':
                print("You have hired "+ai.name+" for "+str(cost)+" gold.")
                party.append(ai)
                playerClass.gold += -cost
                valid = True
            elif hire == 'n':
                print("You motion to the next candidate.")
                valid = True
            else:
                print("Invalid Input")
    print("Your current party is:")
    for member in party:
        print(member.name+", class: "+member.classType+", level:"+str(member.level))

if __name__ == "__main__":
    playerClass = Fighter("Ted", 1, 5, 5, 10, 5, 6, 2, 9)
    playerClass.initPlayer(1)
    party = []
    party.append(playerClass)
    Recruit(playerClass, party)
