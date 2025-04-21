weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the height in cm: "))
BMI = weight/height/100**2
if BMI>=19.9:
    print("You are underweight")
elif BMI>=24.9:
    print("You are healthy")
elif BMI>=29.9:
    print("You are over weight")
elif BMI>=34.9:
    print("You are critically weight")
elif BMI>=39.9:
    print("You are in obese")
else:
    print("You are in severe condition")