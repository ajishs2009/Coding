def total_calc(bill_amt,tip_perc):
    total = bill_amt * (1+0.01*tip_perc)
    total = round(total,2)
    print(f"Total amount is {total}")

total_calc(100,50)