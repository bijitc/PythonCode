# NOT Operator

raining = input("Is it raining? (yes/no): ")

# Boolean
if raining == "yes":
    raining = True  
else:
    raining = False

if raining:
    print("Wear a raincoat.")
if not raining:
    print("Wear a T-shirt.")

