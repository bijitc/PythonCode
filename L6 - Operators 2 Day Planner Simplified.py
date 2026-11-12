# Smart Day Planner

day = input("What day is it? (Monday to Sunday): ")
hw_complete = input("Is your homework done? (yes/no): ")


# Boolean
if hw_complete == "yes":
    hw_complete = True  
else:
    hw_complete = False

print("======== Smart Day Planner ========")

# OR Operator
if day == "Saturday" or day == "Sunday":
    print("Day: Weekend - time to relax!")
    print("Morning: No school today!")
else:
    print("Day: Weekday - stay focused!")
    print("Morning: Reach school on time!")

# NOT Operator
if hw_complete:
    print("Evening: Enjoy your free time!")
if not hw_complete:
    print("Evening: Finish your homework in time!")

# AND Operator
if day == "Sunday" and hw_complete:
    print("Fun Activity: Time to watch a movie!")

print("===================================")
