print("Marvel Movie Character Creator")
print("--")
print()
character=input("'Do you like hanging around'?: ")
if character=="No":
    print("Then you're not \033[32mSpider-man\033[0m")
voice=input("Do you have a 'gravelly' voice?: ")
if voice=="No":
    print("Aww, then you're not \033[33mKorg\033[0m")
feel=input("Do you feel 'Marvelous'?: ")
if feel=="Yes":
    print("Aha! You're \033[36mCaptain Marvel!\033[0m, Hi!")
else:
    print("You are not a superhero")

