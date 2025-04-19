print("Enter the marks of four subjects: ")
hindi = int(input("Hindi marks are: "))
english = int(input("English marks are: "))
maths = int(input("Maths marks are: "))
science = int(input("Science marks are: "))
social = int(input("Social marks are: "))
sum = hindi+maths+english+science+social
perc = sum/400*100
print("Percentage mark:", perc)