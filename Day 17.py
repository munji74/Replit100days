from getpass import getpass as input

print("EPIC 🪨   📃   ✂️    GAME")

p1score=0
p2score=0
while True:
    player1=input("Select your move R, P or S")
    player2=input("Select your move R,P or S")
    print()
    if player1==player2:
        print("You have drawn")

    elif (player1=="R" and player2=="S") or \
        (player1=="S" and player2=="P") or \
        (player1=="P" and player2=="R"):
        p1score+=1
        print("Player1 selected\033[34m",player1,"\033[0mand Player2 selected\033[34m",player2, "\033[0mTherefore \033[32mPlayer1 wins\033[0m")
        print("Player1 wins with a score of:",p1score)
        print()

    elif (player2=="R" and player1=="S") or \
            (player2=="S" and player1=="P") or \
            (player2=="P" and player1=="R"):
        p2score+=1
        print("Player1 selected\033[35m",player1,"\033[0mand Player2 selected\033[35m",player2, "\033[0mTherefore \033[32mPlayer2 wins\033[0m")
        print("Player2 wins with a score of:",p2score)
        print("While player1 had a score of",p1score)
        print()

    if p1score==3 or p2score==3:
        print("Good game")
        break
    else:
        continue

