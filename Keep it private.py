class myclass:
    __privatevar = 27

    def __privMeth(self):   
        print('Im inside the myclass')

    def hello(self):
        print('Private variable value: ',myclass.__privatevar)
foo = myclass()
foo.hello()
foo.__privMeth