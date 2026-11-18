# Correct list -> 10,20,30
# Incorrect list -> 10,50,30
# mean = sum/count or sum = mean*count

count = 3
incorrect_mean = 30

incorrect_number = 50
correct_number = 20

incorrect_sum = incorrect_mean*count
correct_sum = incorrect_sum - incorrect_number + correct_number
correct_mean = correct_sum/count
print("Correct mean value is: ", correct_mean)