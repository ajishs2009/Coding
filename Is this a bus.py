class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class bus(vehicle):
    pass
School_bus = bus('School Volvo', 180, 19)
print('Vehicle name:',School_bus.name,'Max_speed:',School_bus.max_speed,'Mileage:', School_bus.mileage)