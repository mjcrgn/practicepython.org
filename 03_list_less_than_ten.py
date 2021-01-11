'''
210111

https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

03 list less than ten

list, numbers, elements, if, conditional

    take list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print all elements of list less than 5
'''

a = [
       1, 
       1,
       2,
       3,
       5,
       8,
       13,
       21,
       34,
       55,
       89
]

for i in a:
  if i < 5:
    print(i)
  else:
    break

'''
bonus 1:

    make new list that has all elements less than 5 from this list and print out new list
    write this in one line of python
'''

print([aa for aa in a if aa < 5])

'''
Couldn't figure out how to do this in ONE line, so I looked at the solution comments.

  http://disq.us/p/1sv2q9q:

  A list comprehension behaves like this: 
    [output] for [item] in [list] if [filter]

  As you can see there are 4 components in its syntax:
    output, item, list and filter.

  In the case of Sachin's code [aa for aa in a if aa < 5]:

    output = aa
    item = aa
    list = a
    filter = aa < 5

  What this means is that I'm outputting the variable 'aa' which refers to each 
  item in the list (a).

  Since 'aa' is set to refer to each item in list (a), the output will print the 
  items in list (a). However, I also have a filter specified at the end of the 
  code "if aa < 5".

  This means that only the items in the list (referred to as aa) that are below 
  5 are printed out.

  It does help if you use labels that are more intuitive in your code. 
  For example instead of naming the list a, I can name the list "number_list":

    number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

  My list comprehension will go like this:

    [number for number in number_list if number < 5]

  You will get the same output.
'''

# bonus 1, not one line but it works

b = []

for i in a:
  if i < 5:
    b.append(i)

print(b)

'''
bonus 2:

    ask user for #
    return list that contains only elements from original list that are smaller than number given by user
'''

c = []
num = int(input('Enter a number: '))

for i in a:
  if i < num:
    c.append(i)

print(c)