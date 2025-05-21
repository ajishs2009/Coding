class Computer:
    def __init__(self):
        self.__max_price = 900
    def sell(self):
        print('Selling price:{}'.format(self.__max_price))
    def setmaxprice(self,price):
        self.__max_price = price
c = Computer()
c.sell()
c.__max_price = 1000
c.sell()
c.setmaxprice(1000)
c.sell()