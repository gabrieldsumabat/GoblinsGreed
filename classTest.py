from Class.ranger import Ranger
from Class.fighter import Fighter
from Class.cleric import Cleric
from Class.mage import Mage

if __name__=="__main__":
    #Creation
    Bjorn = Fighter("Bjorn", 1, 5, 10, 25, 7, 5, 2, 9)
    Tasla = Ranger("Tasla", 1, 5, 10, 25, 7, 5, 2, 9)
    Charles = Cleric("Charles", 1, 5, 10, 25, 7, 5, 2, 9)
    Siekel = Mage("Seikel", 1, 5, 10, 25, 7, 5, 2, 9)

    #Party
    party = []
    party.append(Bjorn)
    party.append(Tasla)
    party.append(Charles)
    party.append(Siekel)

    #Actions

    # print(Bjorn.name)
    # Bjorn.cleave(Bjorn, party)
    # Bjorn.slash(Bjorn)
    # Bjorn.charge(Bjorn)
    Bjorn.blunt(Bjorn)

    print(Tasla.name)
    Tasla.steelShot(Bjorn, party)
    Tasla.quickShot(Bjorn)
    Tasla.stab(Bjorn)
    Tasla.bullseye()

    # print(Charles.name)
    # Charles.zeal(Siekel)
    # Charles.heal(Charles)
    # Charles.martyr()
    # Charles.pray()
    # Charles.death(party)

    print(Siekel.name)
    Siekel.fireball(Charles, party)
    Siekel.flameBolt(Charles)
    Siekel.lifeleech(party)
    Siekel.channel()

    # print(type(party))
    # Tasla.death(party)
    # for member in party:
    #     print (member.name+", "+member.classType)



