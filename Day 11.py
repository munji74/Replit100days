min=60
hour=60
day=24
secsDay=min*hour*day
daysInYear=365
print("There are",secsDay,"seconds in a day")
print()
year=input("Leap year or Ordinary year: ")
print()
if year=="Ordinary":
    print("There are",secsDay*daysInYear,"seconds in an \033[32mordinary year\033[0m")
elif year=="Leap":
    print("There are",(daysInYear+1)*secsDay,"seconds in a \033[33mLeap year\033[0m")

