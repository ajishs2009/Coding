import math
class circle:
    def ca(self):
        rad = 10
        area = math.pi*rad**2
        return area
    def cp(self):
        rad = 15
        perimeter = 2*math.pi*rad
        return perimeter
area = circle()
print('Area of circle is:', area.ca())
print('Perimeter of circle is:', area.cp())