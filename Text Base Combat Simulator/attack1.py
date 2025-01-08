import random

def attack1():
    hit = int(random.random() * 100)
    if hit <= 24:
        print("Attack missed.")
        attackDamage = 0
    elif hit == 99:
        attackDamage = 10
    else:
        attackDamage = 5
    return attackDamage