# Identity Operators
# is, is not
 
x = 20
y = x
if (x is y):
    print("x & y SAME identity")

x = 20
y = 30
if (x is not y):
    print("x & y have DIFFERENT identity")

x = 5
if (type(x) is int):
    print("true")
else:
    print("false") 