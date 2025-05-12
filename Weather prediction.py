weather = (1,0,0,0,1,1,1)
s = 0
r = 0
for i in range(0,7):
    if (weather[i]==0):
        r+=1
    else:
        s+=1
if(s>r):
    print("Hot weather")
else:
    print("Cool weather")
