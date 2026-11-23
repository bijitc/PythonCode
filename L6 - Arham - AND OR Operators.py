day = input("Enter day of the week: ")
age = int(input("Enter your age: "))

weekend = False

# OR Operator
if day.lower() == "saturday" or day.lower() == "sunday":
    weekend = True
    print("It's weekend! Have fun!")
else:
    print("It's a weekday. Time to work hard!")

# AND Operator
if age >= 10 and weekend:
    print("You can access the pool. Enjoy your swim!")
else:
    print("Swimming not allowed!")


