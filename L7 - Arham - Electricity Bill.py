# Take input of number of units consumed from the user
units = int(input("Enter number of units consumed : "))

# Check conditions of units consumed 
# Then calculate amount and tax accordingly


# Check for units less than 50
if units <= 50:
    amount = units * 2.60 
    tax = 25 

# Check for units less than 100
elif units >50 and units <= 100:
    amount = 50*2.6 + ((units - 50) * 3.25)
    tax = 35

# Check for all the cases other than mentioned 
# When units consumed are more than 100
else:
    amount = 50*2.6 + 50*3.25 + ((units - 100) * 8.45)
    tax = 45

# Calculate and Display the total electricity bill
# total amount = amount + tax
total = amount + tax
print("Electricity Bill: Rs.", total)