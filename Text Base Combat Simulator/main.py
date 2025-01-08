import random
from tutorial import tutorial
from playerTurn import playerTurn
from enemyTurn import enemyTurn
from heal import heal

random.seed()

playerHealth = 50
enemyHealth = int(1 + random.random() * 100)
enemyStartHP = enemyHealth

tutorialIn = input("Is this your first time playing? y/n ")
if tutorialIn == "y":
    tutorial()

print("Player health is: " + str(playerHealth))
print("Enemy health is: " + str(enemyHealth))

while playerHealth > 0 and enemyHealth > 0:
    turnChoiceP = input("Would you like to attack or heal? a/h ")
    
    if turnChoiceP == "a":
        enemyHealth = playerTurn(enemyHealth)
        print("Enemy is on " + str(enemyHealth) + " HP")
    elif turnChoiceP == "h":
        healing = heal()
        playerHealth =+ healing
        if playerHealth > 50:
            playerHealth = 50
        print("Player is on " + str(playerHealth)+ " HP")
    else:
        turnChoiceP = input("Invalid option. Please choose to attack (a) or heal (h) ")
    
    if enemyHealth > 0:
        if enemyHealth < (enemyStartHP / 2):
            turnChoiceE = int(random.random() * 3)
            if enemyHealth == 5 and playerHealth > 10:
                if turnChoiceE == 0 or turnChoiceE == 1:
                    healing = heal()
                    enemyHealth =+ healing
                    if enemyHealth > 50:
                        enemyHealth = 50
                    print("Enemy is on " + str(enemyHealth) + " HP")
                else:
                    playerHealth = enemyTurn(playerHealth)
                    print("Player is on " + str(playerHealth) + " HP")
            elif turnChoiceE == 2:
                healing = heal()
                enemyHealth =+ healing
                if enemyHealth > 50:
                    enemyHealth = 50
                print("Enemy is on " + str(enemyHealth) + " HP")
            else:
                playerHealth = enemyTurn(playerHealth)
                print("Player is on " + str(playerHealth) + " HP")
        else:
            playerHealth = enemyTurn(playerHealth)
    print("Player is on " + str(playerHealth) + " HP")

if playerHealth > 0:
    print("Enemy defeated. You Won!")
else:
    print("Player defeated. You Lost!")