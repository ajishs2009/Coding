try:
   num1, num2 = eval(input("Enter the two numbers, separated with a comma: "))
   result = num1/num2
   print("The result is: ",result)
except ZeroDivisionError:
    print("Division by zero is error!!")
except SyntaxError:
    print("The two numbers are not separated by comma")
except:
    print("No Value")
else:
    print("No Exceptions")
finally:
    print("This will be printed anyways")