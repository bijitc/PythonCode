minimum_age = 10
age = int(input("Enter your age: "))

if age >= minimum_age:
    print("You are old enough to swim in the pool.")
else:
    print("You are not old enough to swim in the pool.")

status = "open"

if status and age >= minimum_age:
    print("The swimming pool is open and you can swim.")