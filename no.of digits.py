num = int(input("Enter a number: "))
digit = 0
while num!=0:
    num//=10
    digit = digit+1
print("the number of digits is:",digit)
