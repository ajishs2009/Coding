medic_cause = input("Enter if you have medical cause Y or N ")
attend = input("Enter the attendance of student")
if medic_cause == 'Y':
    print("You are allowed")
else:
    if attend>=75:
        print("You are allowed")
    else:
        print("You aren't allowed")

