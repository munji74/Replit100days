print("Exam Grade Calculator")
exam=input("Name of the exam: ")
print()
maxScore=int(input("Enter the maximum score: "))
print()
totalScore=int(input("Enter your score: "))
percentScore=float(totalScore/maxScore)*100
round(percentScore, 2)
# print(percentScore)
if (percentScore<=100 and percentScore>=90):
    print("You got",round(percentScore,2),"in the",exam,"exam which is an A+ğ")
elif (percentScore<=89 and percentScore>=80):
    print("You got",round(percentScore,2),"in the",exam,"exam which is an Ağ¥³")
elif (percentScore<=79 and percentScore>=70):
    print("You got",round(percentScore,2),"in the",exam,"exam which is a Bğ")
elif (percentScore<=69 and percentScore>=60):
    print("You got",round(percentScore,2),"in the",exam,"exam which is a Cğ")
elif (percentScore<=59 and percentScore>=50):
    print("You got",round(percentScore,2),"in the",exam,"exam which is a Dğ")
elif (percentScore<=49 and percentScore>=0):
    print("You got",round(percentScore,2),"in the",exam,"exam which is a Uğ¢")
else:
    print("A score of",round(percentScore,2),"is impossible")

