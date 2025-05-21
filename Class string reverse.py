class String:
    def __init__(self,string):
        self.string = string
    def revString(self):
        return self.string[::-1]
str = String('Ajish')
print(str.revString())
