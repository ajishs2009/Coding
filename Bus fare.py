class Vehicle:
    def __init__(self,fare,seats):
        self.fare = fare
        self.seats = seats
    def fare(self):
        print('Total fare is {}'.format(self.fare,self.seats))