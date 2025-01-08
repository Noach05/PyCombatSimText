import random

def attack2():
    hit = int(random.random() * 100)
    if hit <= 49:
        print ("Attack missed.")
        attackDamage = 0
    elif hit == 99:
        attackDamage = 20
    else:
        attackDamage = 10
    return attackDamage