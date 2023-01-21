print("This is my guess my favourite sport game")
print()
counter = 0
while True:
    sport = input("My favourite sport is: ")
    if sport=="football":
        print("Nicely guessed!")
    else:
        print("Wrong! Try again!")
    counter += 1
    if sport=="football":
        break
print("Thanks for playing!")
print("Total guesses= ", counter)