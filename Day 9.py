print("Generation Identifier")
print("\033[36m------------------------------------------------\033[0m")
yob=int(input("Which year were you born? "))
if yob >=1883 and yob<=1900:
    print("Lost Generation")

elif yob >= 1901 and yob<=1927:
    print("Greatest Generation")

elif yob >= 1928 and yob<=1945:
    print("Silent Generation")

elif yob >= 1946 and yob<=1964:
    print("Baby Boomers")

elif yob >= 1965 and yob<=1980:
    print("Generation X")

elif yob >= 1981 and yob<=1996:
    print("Millenials")

elif yob >= 1997 and yob<=2012:
    print("Generation Z")

elif yob >= 2013 and yob<=2030:
    print("Generation Alpha")
    
else:
    print("Generation has no name")