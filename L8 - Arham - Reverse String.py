#Input a word or sentence
string = input("Please enter your own String : ")

string2 = ('')
#loop for printing in reverse 
for x in string:
    string2 = x + string2
    
print("Original String = ", string)
print("Reversed String = ", string2)
