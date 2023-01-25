import random
print("ONE-TO-MILLION GAME")
print()
number=random.randint(1,1000000)
guesses=0
while True:
    guess=int(input("Guess the number: "))
    if guess<0:
        print("Oooh wrong number.")
        exit()
    if guess>number:
        print("Too high")
        guesses+=1
        continue
    elif guess<number:
        print("Too low")
        guesses+=1
        continue
    elif guess==number:
        print("Winner🥳🥳🥳")
        guesses+=1
        break
    
    else:
        print("That is a wrong number")
if guesses==1:
    print("It took",guesses,"attempt to get the right number")
else:
    print("It took",guesses,"attempts to get the right number")
  

  
  