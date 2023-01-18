exit = ""
while exit != "yes":
    animal=input("What animal do you want?: ")
    if animal=="cow":
        print("Cow goes Moo")
        exit = input("Exit?: ")
        if exit=="yes":
            print("Good bye 👋")
    elif animal=="goat":
        print("goat goes behh")
        exit = input("Exit?: ")
        if exit=="yes":
            print("Good bye 👋")
    elif animal=="dog":
        print("Dog says woof")
        exit = input("Exit?: ")
        if exit=="yes":
            print("Good bye 👋")
    elif animal=="cat":
        print("Cat 🙀 says meow")
        exit = input("Exit?: ")
        if exit=="yes":
            print("Good bye 👋")  
    else:
        print("I dont know the sound of that animal")
    