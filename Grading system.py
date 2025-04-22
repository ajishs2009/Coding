markOne = int(input('Enter mark: '))
markTwo = int(input('Enter mark: '))
markThree = int(input('Enter mark: '))
markFour = int(input('Enter mark: '))
markFive = int(input('Enter mark: '))
tot = markOne+markTwo+markThree+markFour+markFive
average = tot/5
if average>=91 or average<=100:
    print("Your grade is A1")
elif average>=81 or average<=91:
    print("Your grade is A2")
elif average>=71 or average<=81:
    print( "Your grade is B1")
elif average>=61 or average<=71:
    print("Your grade is B2")
elif average>=51 or average<=61:
    print("Your grade is C1")
elif average>=41 or average<=51:
    print("Your grade is C2")
elif average>=31 or average<=41:
    print("Your grade is D")
elif average>=21 or average<=31:
    print("Your grade is E1")
elif average>=11 or average<=21:
    print("Your grade is E2")
else:
    print("Invalid input")
