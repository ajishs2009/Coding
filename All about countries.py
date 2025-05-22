class INDIA:
    def capital(self):
        print('New delhi')
    def language(self):
        print('Mostly hindi')
    def type(self):
        print('Developing country')
class USA:
    def capital(self):
        print('Washington DC')
    def language(self):
        print('English')
    def type(self):
        print('Developed country')
obj_ind = INDIA()
obj_usa = USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()

    