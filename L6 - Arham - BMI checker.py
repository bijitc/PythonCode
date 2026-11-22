height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI_index = weight / (height/100)**2

print("Your BMI is: ", BMI_index)

if BMI_index >= 18.5 and BMI_index <=24.9:
    print("You are healthy!")
elif BMI_index < 18.5:
    print("Eat more!")
else:
    print("You need to workout!")

