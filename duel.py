import os
import random
import player

class duel:
    def __init__(self, attacker, defender, state):

        self.attacker = attacker
        self.defender = defender
        self.state = state


        self.id = str(random.getrandbits(50))

        with open(str(self.id)+".txt",'x') as f:
            f.write(str(self.id)+"\n")
            f.write(str(self.attacker)+"\n")
            f.write(str(self.defender)+"\n")
            f.write(str(self.state)+"\n")

async def create(attacker,defender):
    a = duel(attacker,defender,"active")

    atk = player.FindPlayerById(attacker)
    atk.infight = a.id

    defn = player.FindPlayerById(defender)
    defn.infight = a.id

    player.SaveCondition(atk)
    player.SaveCondition(defn)

    return a

def close(duelID):
    with open(duelID+ ".txt") as f:
        a = list(f)
        atk = player.FindPlayerById(a[1].strip())
        defn = player.FindPlayerById(a[2].strip())

    atk.infight = "NOT"
    defn.infight = "NOT"

    player.SaveCondition(atk)
    player.SaveCondition(defn)

    os.remove(duelID+ ".txt")