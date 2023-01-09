print("MY LOGIN SYSTEM")
print("++++++++++++++++")
username=input("Username: ")
password=input("Password: ")
print()

if username=="David" and password=="david":
  print("""Hello there David, What a lovely accent  you have,you could have charmed your way inhere     even without a password.

Have a great day.

Dont forget to wear a hat in the sun!
""")
  print()

elif username=="John" and password=="john":
  print("""Welcome John, Looking Sharp today
I hope you're ready to smash the day
""")
  print()
elif username=="Jane" and password=="jane":
  print("""Welcome Jane, you're a champion
And you like you're ready to attack the day,
And do cool stuff
""")
else:
  print("Wrong Password or Username, You're not allowed to access the system")
