import random

def attack3():
    hit = int(random.random() * 100)
    if hit <= 74:
        print("Attack missed.")
        attackDamage = 0
    elif hit == 99:
        attackDamage = 30
    else:
        attackDamage = 15
    return attackDamage