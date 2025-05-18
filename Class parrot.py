class parrot:
    species = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = parrot('blu',5)
woo = parrot('woo',4)
print('Blu is a {}'.format(blu.species))
print('Woo is a {}'.format(woo.species))
print("Blu is {} years old.".format(blu.age))
print("Woo is {} years old.".format(woo.age))
