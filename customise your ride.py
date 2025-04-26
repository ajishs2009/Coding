print("Select your ride: ")
print("1.Bike")
print("2.Car")
choice = int(input("Enter your choice"))
if choice==1:
    print("Choose the options")
    print("1.Scooty")
    print("2.Scooter")
    choice_2 = input("Enter your choice")
    if choice_2==1:
     print("You have selected scooty")
    else:
     print("You have selected scooter")

elif (choice)==2:
   print("What type of car? ")
   print("Sedan")
   print("XUV")
   choice_3 = int(input("Enter your choice: "))
   if choice_3 == 2:
    print("You have selected sedan")
   else:
    print("You have selected XUV")
else:
  print("Wrong option")