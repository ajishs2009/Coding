num = int(input('Enter a series of numbers: '))
odd_num = [i for i in range(num) if i%2!=0]
print('Odd numbers are:', odd_num)
even_num = [i for i in range(num) if i%2==0]
print('Even numbers are:', even_num)
fruits = ['apple','banana','orange','grapes']
Fruits = [x[0].upper()+x[1:] for x in fruits]
print('fruits as proper nouns:', Fruits)