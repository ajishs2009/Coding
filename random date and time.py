import random
import time
def getRandom(startDate,endDate):
    print("Print random date between startDate and endDate:")
    randomGenerator = random.random()
    date_format = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate,date_format))
    endTime = time.mktime(time.strptime(endDate,date_format))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(date_format, time.localtime(randomTime))
    return randomDate
print("Random date = ", getRandom('1/1/2016','12/12/2018'))