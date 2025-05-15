s1 = {2,1,3}
s2 = {'x','z','y'}
s3 = list(zip(s1,s2))
print(s3)
s1 = [10,20,30,40]
s2 = [100,200,300,400]
for x,y in zip(s1,s2[::-1]):
    print(x,y)
stocks = ['Reliance', 'Infoxys']
prices = [2010,2020]
new_dict = {stocks:prices for stocks,prices in zip(stocks,prices)}
print(new_dict)
