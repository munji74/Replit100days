print("Wholesome Positivity Machine")
print()
name=input("Who are you?: ")
if name=="Munji" or "David" or "Jane" or "Michael" or "Michelle":
    achieve=input("What do you want to achieve?: ")
    if achieve=="learn code":
        feel=input("On a scale of 1 - 10 how do you feel today?(1:😢 , 10:🥳): ")
        feel=int(feel)
        if feel >= 6 and feel <= 10:
            print("-------------------------------------------")
            print("Hey\033[34m",name,"\033[0mwell done champ! Today is going to be a very beautiful day, you are going to achieve alot thanks to your\033[35m", feel , "out of 10\033[0m feeling, You are going to\033[32m",achieve,"\033[0mtoday")
        elif feel <6 and feel >= 0 :
            print("-------------------------------------------")
            print("Hey\033[34m",name,"\033[0mI know life can be hard but today is beautiful, you have to treasure it your\033[35m", feel , "out of 10\033[0m feeling has alot of potential to be better, you are going to\033[32m",achieve,"\033[0mtoday")
        else:
            print("-------------------------------------------")
            print("Enter a number between \033[31m1-10\033[0m")
    else:
        print("------------------------------------------")
        print("You should 'learn code'")
else:
    print("------------------------------------------")
    print("Enter Munji")
    print("------------------------------------------")