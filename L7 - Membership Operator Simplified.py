# Membership Operators
maths = 90
english = 95

total = maths + english 
avg = int(total / 2)

validRange = range(0, 101)

if avg not in validRange:
    print("Invalid Input!")
elif avg in range(91, 101):
    print("Your Grade is A1")
else:
    print("Try harder next time!")