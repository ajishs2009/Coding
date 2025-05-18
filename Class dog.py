class dog:
    species1 = 'Doberman'
    species2 = 'Pitbull'
    def __init__(self, name, age):
        self.name = name
        self.age = age
Tom = dog('Tom',7)
Jerry = dog('Jerry',5)
print('Tom is a {}'.format(Tom.species1))
print('Jerry is a {}'.format(Jerry.species2))
print("Tom's age is {}".format(Tom.age))
print("Jerry's age is {}".format(Jerry.age))