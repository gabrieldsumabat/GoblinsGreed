from Menu.newGame import newGame
from Quest.Guild.recruit import Recruit


if __name__ == "__main__":
    playerClass = newGame()
    party = []
    party.append(playerClass)
    Recruit(playerClass, party)
#    Loop the GUILD > QUEST > FIGHT > REWARD > REPEAT
