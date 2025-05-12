def SquaredNumber(beg,end):
    lst = []
    for i in range(beg,end):
        lst.append(i**2)
    lst_even = []
    lst_odd = []
    for i in lst:
        if i%2==0:
            lst_even.append(i)
        else:
           lst_odd.append(i)
    print("The square of even numbers are: ",lst_even)
    print("The square of odd numbers are: ",lst_odd)

SquaredNumber(2,10)

