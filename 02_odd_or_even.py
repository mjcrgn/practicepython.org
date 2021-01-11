'''
210110

https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

02 odd or even

input, if, types, int, equality, comparison, numbers, mod

    ask user for #
    print appropriate msg that number is even or odd

bonus 1:

    if # is multiple of 4, print out different msg
'''

oddOrEven = int(input('Enter a number: '))

if oddOrEven % 4 == 0: # check bonus 1 first
  print(str(oddOrEven), 'is even and divisible by 4.') 
elif oddOrEven % 2 == 0:
  print(str(oddOrEven), 'is even.')
else:
  print(str(oddOrEven), 'is odd.')

'''
bonus 2:

    ask for two #s: one to check (call it num), one to divide (check)
    if check divides evenly into num, tell that to user. if not, print appropriate msg
'''

num = int(input('Enter an integer: '))
check = int(input('Enter another integer: '))

if check % num == 0:
  print(f'{num} is divisible by {check}.') # trying f-strings
else:
  print(f'{num} is NOT divisible by {check}.')