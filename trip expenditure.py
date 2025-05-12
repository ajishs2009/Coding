def hotel_cost(night):
    return 140*night
def plane_cost(city):
    if 'Charlotte'==city:
        return 183
    elif 'Tampa'==city:
        return 220
    elif 'Pittsburg'==city:
        return 222
    elif 'Los Angeles'==city:
        return 475
def rent_car(days):
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else:
        return 40*days

print("Cost of rent car:", rent_car(5))
print("Cost of hotel:", hotel_cost(5))
print("Cost of plane ticket:", plane_cost("Los Angeles"))
