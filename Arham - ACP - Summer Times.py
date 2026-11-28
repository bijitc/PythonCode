temperature = int(input("Enter the temperature: "))

if temperature < 15:
    print("Wear thick woolen clothes to keep yourself warm!")
elif temperature > 15 and temperature < 20:
    print("Wear a jacket or hoodie to keep you away from cold!")
elif temperature > 20 and temperature < 25:
    print("This is about the normal temperature wear you can wear anything you're comfortable with!")
else:
    print("Wear light clothes so you don't sweat!")