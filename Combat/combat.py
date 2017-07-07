import time


def combat(party, enemy):
    turn = party + enemy
    ongoing = True
    while ongoing is True:
        for member in turn:
            if member.enemy == True:
                targets = party
                allies = enemy
            elif member.enemy == False:
                targets = enemy
                allies = party
            member.calculateAction(targets, allies)
            if member.target is not None:
                if member.target.hp <= 0 and member.target.enemy is False:
                    member.target.death(party)
                elif member.target.hp <= 0 and member.target.enemy is True:
                    member.target.death(enemy)
            if party == []:
                print("The party has been slain!")
                result = False
                ongoing = False
                # GAME OVER
            elif enemy == []:
                print("Quest Success")
                result = True
                ongoing = False
            time.sleep(5)

