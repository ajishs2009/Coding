test_dict = {'Codingal':2, 'is':2,'best':2,'for':2,'coding':1}
res = 0
K = 2
for key in test_dict:
    if test_dict[key] == K:
        res = res+1
print('Frequency is: ',res)
