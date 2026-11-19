height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print("Your BMI is: ", BMI)

if BMI >= 18.5 and BMI <=24.9:
    print("You are healthy!")
elif BMI < 18.5:
    print("Eat more!")
else:
    print("You need to workout!")

