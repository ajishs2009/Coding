import random
playing = True
number = str(input(random.randint(10,20)))
print("enter a number between 10 and 20: ")
print('the game ends if you guess the number correct')
while playing:
    guess = input("Enter your guess: ")
    if number == guess:
        print("You won the game!")
        print("The number is", number)
        break
    else:
        print("You have guessed it wrong!")
