print("Login System")
print()
def login():
    while True:
        username=input("What is your username? ")
        password=int(input("What is the password? "))
        if username=="Munji" and password==12345:
            print("Welcome to the system", username, "Your credentials are correct")
            break
        else:
            print("Those details are wrong. Please try again.")
            continue

login()
  
  