print("ONE-TO-MILLION GAME")
print()
number=52500
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
print("It took",guesses,"attempts to get the right number")
  

  
  