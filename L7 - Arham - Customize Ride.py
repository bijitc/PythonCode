print("Select your ride: ")
print("1. Bike")
print("2. Car")

#take input of number 1 or 2
#select your ride
type = int( input("Enter your choice: ") )

# option 1 outer if
if type == 1:
  print( "what type of bike? " )
  print("1.Scooty\n")
  print("2.Scooter\n")
  #option 1 nested/inner if
  #Condition for selecting the type of bike
  subtype = int(input("Enter you choice: "))
  if subtype == 1:
    print("you have selected scooty")
  else:
    print("you have selected scooter")


# option 2 outer if
if type == 2:
  print( "what type of car?" )
  print("1.Sedan")
  print("2.XUV")
  subtype = int(input("enter your choice: "))
  #option 2 nested/inner if
  if subtype == 1: 
    print("you have selected sedan")
  else:
    print("you have selected XUV")
