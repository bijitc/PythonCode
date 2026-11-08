# PART 1: Ask for today's temperature
temperature = int(input("Enter today's temperature in Celsius: "))

# PART 2: Decide between a jacket and a t-shirt
if temperature < 25:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is pleasant today.")
    print("Wear a", outfit)

# PART 3: Ask whether it is raining
is_raining = input("Is it raining today? (yes/no): ")

# PART 4: Add an umbrella reminder only if it is raining
if is_raining == "yes":
    print("Bring an umbrella!")


print("Weather check complete!")

# PART 10: Print the final outfit summary
print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Carry Umbrella:", is_raining)
print("===================================")
