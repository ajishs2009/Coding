class Flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'( '+self.meaning+')'

flash = []
print('Welcome to flashcard application')
while(True):
    word = input('Enter the word: ')
    meaning = input('Enter the meaning: ')

    flash.append(Flashcards(word,meaning))
    option = int(input('enter 0, if you want to add another word. Otherwise enter 1'))
    if(option):
        break
print('Your Flashcards')
for i in flash:
    print('>', i)