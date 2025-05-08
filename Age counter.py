try:
   age = int(input("Enter the age: "))
   if age<0:
       print("Age can't be lesser than 0")
   elif age%2==0:
      print("Age is an even number")
   else:
      print("Age is an odd number")
except ValueError:
     print("Invalid input")
