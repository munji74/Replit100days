import random
def dice(sides):
    result= random.randint(1,sides)
    return result

def dice6_8():
    side6_dice=dice(6)
    side8_dice=dice(8)
    health = side6_dice * side8_dice
    return health

character="yes"

while character=="yes":
    character1=input("Name your character: ")
    health=str(dice6_8())
    print("Their health is",health,"hp")
    character=input("Another character?")
    
  