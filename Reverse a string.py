string = str(input("Enter a string: "))
string_2 = ''
for i in string:
    string_2 = i+string_2
print("The original string is: ", string)
print("The reversed string is: ", string_2)