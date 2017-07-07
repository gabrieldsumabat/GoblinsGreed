from Class.fighter import Fighter
from Class.ranger import Ranger
from Class.cleric import Cleric
from Class.mage import Mage
from random import randint


def newGame():
    """Creates a new player and initializes all values for the player character"""
    print("Welcome to Goblins Greed!")
    print("Please enter a player name:")
    name = input()
    print("Please enter the difficulty level from 1 - 5 with 1 being the easiest and 5 being the hardest.")
    valid = False
    while valid is False:
        try:
            difficulty = input()
            difficulty = int(difficulty)
            if 1 <= difficulty <= 5:
                print("Difficulty level is set to " + str(difficulty))
                valid = True
            else:
                print("Invalid input, please try again.")
        except ValueError as e:
            print("Input is not an integer!")

    print("""Please enter the class you would like to play: 
                1. Fighter
                2. Ranger
                3. Cleric
                4. Mage
            """)
    valid = False
    classSelect = {1: "Fighter", 2: "Ranger", 3: "Cleric", 4: "Mage"}
    while valid is False:
        try:
            playerClass = input()
            playerClass = int(playerClass)
            if 1 <= playerClass <= 4:
                playerClass = classSelect[playerClass]
                print(playerClass+" is selected!")
                valid = True
            else:
                print("Invalid input, please try again.")
        except ValueError as e:
            print("Input is not an integer!")
#                       name, level, alignment, trust, maxHp, morale, dmg, armour, greed ++UPDATE VALUES AND DECIDE
    if playerClass == "Fighter":
        playerClass = Fighter(name, 1, randint(1, 10), 10, randint(1, 6)+5, randint(1, 6)+5, randint(3, 7)
                              , randint(2, 4), randint(1, 3))
    elif playerClass == "Ranger":
        playerClass = Ranger(name, 1, randint(1, 10), 10, randint(1, 6) + 5, randint(1, 6) + 5, randint(4, 6),
                              randint(1, 2), randint(1, 3))
    elif playerClass == "Cleric":
        playerClass = Cleric(name, 1, randint(5, 10), randint(5, 15), randint(1, 3)+4, randint(3, 6)+5, randint(2, 4)
                             , randint(1, 3), randint(1, 5))
    else:
        playerClass = Mage(name, 1, randint(1, 5), randint(5, 10), randint(1, 3)+4, randint(3, 10),
                           randint(5, 15), randint(0, 4), randint(5, 10))
    playerClass.initPlayer(difficulty)
    return playerClass
