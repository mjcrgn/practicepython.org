'''
210111

https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

04 divisors

    ask for #
    print list of all divisors of #
'''

num = int(input('Enter a number: '))
ints = list(range(1, num + 1))
divisors = []

# check if [1, num] divide equally into num 
for i in ints:
  if num % i == 0:
    divisors.append(i)

print('The following are divisors of ' + str(num) + ':', divisors)