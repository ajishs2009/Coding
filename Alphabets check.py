c = input("Enter a character: ")
if c>='0' and c<='9':
    print("\n It is a number")
elif c>='a' and c<='z':
    print("\n It is an alphabet")
elif c>='A' and c<='Z':
    print("It is an Alphabet")
else:
    print("It is neither an integer nor an alphabet")