#input an integer value 
n = int(input("Enter the number whose sum you want to find: "))

sum = 0

#Iterates for n times
#range(start, stop, step)
for i in range(1, n+1, 1): 
  sum += i

print("Sum: ", sum)