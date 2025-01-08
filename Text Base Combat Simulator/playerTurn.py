from attack1 import attack1
from attack2 import attack2
from attack3 import attack3

def playerTurn(enemyHealth):
    attackChoice = int(input("Choose an attack: 1/2/3 "))
    
    while attackChoice != 1 and attackChoice != 2 and attackChoice != 3:
        attackChoice = int(input("Invalid attack choice. Please choose form 1/2/3: "))
    if attackChoice == 1:
        print("You chose: Knife Yeet")
        attackDamage = attack1()
    elif attackChoice == 2:
        print("You chose: Ol' Betsy")
        attackDamage = attack2()
    else:
        print("You chose: Hammah!")
        attackDamage = attack3()
    print("Player dealt " + str(attackDamage) + " HP damage")
    enemyHealth -= attackDamage
    return enemyHealth