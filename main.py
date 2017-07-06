from Menu.newGame import newGame
from Quest.Guild.guid import guild


if __name__ == "__main__":
    playerClass = newGame()
    party = []
    party.append(playerClass)
    guild(playerClass, party)
#    Loop the GUILD > QUEST > FIGHT > REWARD > REPEAT
