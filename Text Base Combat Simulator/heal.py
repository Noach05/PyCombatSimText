import random

def heal():
    healType = int(random.random() *8)
    if healType == 0 or healType == 1 or healType == 2:
        heal = 5
        print(str(heal) + " HP healed")
    elif healType == 3 or healType == 4:
        heal = 10
        print(str(heal) + " HP healed")
    elif healType == 5:
        heal = 15
        print(str(heal) + " HP healed")
    else:
        heal = 0
        print("Healing failed")
        print(str(heal) + " HP healed")
    
    return heal
    