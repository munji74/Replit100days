import random
print("Dice Game")
print()

sides=int(input("How many sides:"))
game="yes"

def rollDice(sides):
    print("You rolled", random.randint(1,sides))

while game=="yes":
    rollDice(sides)
    game=input("Roll again?: ")