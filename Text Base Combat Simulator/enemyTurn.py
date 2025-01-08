import random
from attack1 import attack1
from attack2 import attack2
from attack3 import attack3

def enemyTurn(playerHealth):
    attackChoice = int(random.random() * 6)
    if attackChoice == 0 or attackChoice == 1 or attackChoice == 2:
        print("Enemy chose: Kitty Eyes (Awwh)")
        attackDamage = attack1()
    elif attackChoice == 3 or attackChoice == 4:
        print("Enemy chose: slap")
        attackDamage = attack2()
    else:
        print("Enemy chose: Look of disappointment")
        attackDamage = attack3()
    
    print ("Enemy dealt " + str(attackDamage) + " HP damage")
    playerHealth -= attackDamage
    return playerHealth