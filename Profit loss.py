actual_cost = float(input("Enter the actual amt: "))
selling_cost = float(input("Enter the selling amt: "))
if(selling_cost > actual_cost):
    amount = selling_cost - actual_cost
    print("Profit: ", amount)
else:
    print("No profit..!")