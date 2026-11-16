# Membership Operators
score1 = 90
score2 = 95

total = score1 + score2 
avg = int(total / 2)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid Input!")
elif avg in range(91, 101):
    print("Your Grade is A1")
else:
    print("Try harder next time!")