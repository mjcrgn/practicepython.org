'''
210110

https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

01 character input

input, strings, types, int

    ask user to enter name and age
    print msg telling them year they will turn 100
'''

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
had_birthday = input('Have you celebrated your birthday this year? Enter Y or N: ')

if had_birthday == 'Y':
  print('You will turn 100 years old in the year', str(2021 - age + 100) + '.')
else:
  print('You will turn 100 years old in the year', str(2021 - age + 99) + '.')

'''
bonus:

    ask user for another #, print out that many copies of previous msg on separate lines
'''

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
had_birthday = input('Have you celebrated your birthday this year? Enter Y or N: ')
repeat = int(input('Enter a positive integer: '))

if had_birthday == 'Y':
  print(repeat * ('You will turn 100 years old in the year ' + str(2021 - age + 100) + '.\n'))
else:
  print(repeat * ('You will turn 100 years old in the year ' + str(2021 - age + 99) + '.\n'))
    # unlike above these repeats only work with concatenation

# testing string multiplication

print(3 * 'Hello\n')
print(3 * ('Hello' + '.\n'))
print(3 * ('Hello', '.\n'))