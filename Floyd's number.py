print("Floyd's number")
rows = int(input("Enter the number of rows: "))
num = 0
for i in range(0,rows+1):
    for j in range(0,i+1):
        print(num, end=' ')
        num = num+1
    print()