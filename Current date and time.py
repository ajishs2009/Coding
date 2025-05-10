from datetime import date , time , datetime
today = date.today()
time = datetime.now()
print("Today's date is: ",today)
print("Today's time is: ",time)
print("Date components are, ", today.year, today.month, today.day)