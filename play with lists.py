L = [4,5,1,3,2,7,9,10,8]
print("The original list is:", L)
count = 0
for i in L:
    count+=i
avg = count/len(L)
print("The sum is: ",count)
print("The average is: ",avg)
L.sort()
print("The smallest number in the list is: ",L[0])
print("The largest number in the list is: ",L[-1])