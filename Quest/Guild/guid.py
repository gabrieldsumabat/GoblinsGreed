from Quest.Guild.tavern import Recruit

def guild(playerClass, party):
    """Platform for general guild functions"""
    print("\nWelcome to the GUILD. There are several key areas available to you as a member. \n\n"
          "1. The Tavern. Pretty coins for new faces.\n"
          "2. Greedy Fingers. Your blood, sweat and tears for gold.\n"
          "3. The Hound. The endless list of heads to fetch. \n\n")

    print("Which area would you like to enter? (1/2/3)")
    valid = False
    while valid == False:
        try:
            area = input()
            area = int(area)
            if 1 <= area <= 3:
                valid = True
            else:
                print("Invalid input, please try again.")
        except ValueError as e:
            print("Input is not an integer!")
    if area == 1:
        if playerClass.gold < 30:
            print("Without the gold to recruit, you doubt you'll find a warm welcome there.")
            guild(playerClass, party)
        elif len(party) == 3:
            print("With a full party, you have no reason to re-enter the tavern.")
            guild(playerClass, party)
        else:
            Recruit(playerClass, party)
            guild(playerClass, party)
    else:
        print("Not Implemented Yet")