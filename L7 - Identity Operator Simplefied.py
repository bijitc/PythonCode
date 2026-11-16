# Identity Operators
# is, is not
 
x = 20
y = x 
if (x is y):
    print("x & y have same identity")

x = 20
y = 30
if (x is not y):
    print("x & y have different identity")

x = 5
if (type(x) is int):
    print("x is an Integer")
else:
    print("x is not an Integer") 