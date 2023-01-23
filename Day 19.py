borrowed = 1000.0
rate=0.05
for i in range(10):
    borrowed += (borrowed*rate)
    print("Year",i+1, "is", round(borrowed,2))