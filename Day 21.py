number=int(input("Enter a number: "))
print()
points=0
for i in range(1,11):
    correct=i*number
    print("\033[32m",i, "x",number, "\033[0m")
    answer=int(input("Give me your answer: "))
    if correct==answer:
        print("Thats right")
        points +=1
    else:
        print("That is wrong")
        print("The right answer is\033[33m", correct ,"\033[0m")
    if points==10:
        print("Well done. You got a perfect 10 ")
    else:
        print("You got a score of\033[32m",points,"/ 10\033[0m")

