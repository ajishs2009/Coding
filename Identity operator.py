x = 5
if type(x) is int:
    print(x, "is an integer")
x = 6.7
if type(x) is float:
    print(x, "is a decimal")
x = 20
y = 20
if x is y:
    print("Both are equal")
y = 30
if x is y:
    print("both are same")
else:
    print("Both are different")