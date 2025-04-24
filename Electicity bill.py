units = int(input("Enter the no. of units consumed: "))
if units<50:
    amount = units*2.60
    surcharge = 25
elif units<=100:
    amount = 130 + ((units-50)*3.25)
    surcharge = 45
elif units<=200:
    amount = 130+162.50+526+((units-100)*5.26)
    surcharge = 60
else:
    amount = 130+162.50+526+((units-200)*8.45)
    surcharge = 80
print("Total charge is %.2f" %amount)