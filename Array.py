import array as arr
array_num = arr.array('i',(1,2,3,4,3,5,6,3))
print(array_num)
print("Number of occurences of number 3 is: ",array_num.count(3))
array_num.reverse()
print(array_num)
