#using try and except
try:
   number = int(input('Enter a number: '))
   print("The number is: ",number)
except ValueError as ey:
   print("The error is: ",ey)
   


