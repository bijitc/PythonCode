# Farm Harvest Calculator

# PART 1: Assignment Operator (=)
field1 = 10
field2 = 20
field3 = 30

# PART 2: Arithmetic Operator(+, -, *, /) 
total   = field1 + field2 + field3 # addition operator
average = total / 3 # division operator
print("Average harvest ", average)

price_per_kg = 5
income = total * price_per_kg # multiplication operator
print("Total income ", income)

# PART 3: Comparison Operators (>, <, ==, >=)
# Compare this year's harvest with last year
last_year = 50
print("Better than last year? ", total > last_year)

# PART 4: More Assignment Operators
bonus = 15
# income = income + 15 # updating a variable
income += 15 # Increment
print("Income after bonus:", income)

# PART 5: More Arithmetic Operators
# Floor division and Remainder
# Each bag can hold 7 kg of harvest. Calculate number of full bags and leftover grain.
bags     = total // 7
leftover = total % 7

print("Full bags packed ", bags)
print("Leftover grain ", leftover)


