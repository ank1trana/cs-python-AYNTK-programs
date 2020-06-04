#easier or more readable way to lists

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
  my_list.append(n)
print(my_list)
#>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([n for n in nums])
#>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print('############### ############ ############ ############')
# I want 'n*n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)
#>>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print('############### ############LIST COMPREHENSIBLE WAY  ############ ############')
my_list = [n*n for n in nums]
print(my_list)
'''
############### ############LIST COMPREHENSIBLE WAY  ############ ############
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

print('############### ############ using maps and lambda : one liner  ############ ############')
#map runs everything in a list through a certain function
#lambda is anonymous func
# Using a map + lambda
my_list = list(map(lambda n: n*n, nums))
print(my_list)
#>>> 
print('############### ############ ANOTHER EXAMPLE  ############ ############')
# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)
#>> [2, 4, 6, 8, 10]
print('############### ############ SAME EXAMPLE  USING LIST COMPREHENSION  ############ ############')

my_list = [n for n in nums if n%2 == 0]
print(my_list)
'''
############### ############ SAME EXAMPLE  USING LIST COMPREHENSION  ############ ############
[2, 4, 6, 8, 10]
'''
print('############### ############ again using maps and lambda : one liner  ############ ############')
# Using a filter + lambda and no use of map here
my_list = list(filter(lambda n: n%2 == 0, nums))
print(my_list)
#>> [2, 4, 6, 8, 10]



# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)

'''
[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]
'''

#LIST COMPRESENSION WAY:-

my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)

'''
[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3), ('d', 0), ('d', 1), ('d', 2), ('d', 3)]
letter should be called letter in the loop, and so should be the case for num
'''

print('^^^^^^^^^^^^^^ Dictionary Comprehensions   ^^^^^^^^^^^^^^^^^')
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print(list(zip(names, heros)))
'''^^^^^^^^^^^^^^ Dictionary Comprehensions   ^^^^^^^^^^^^^^^^^
[('Bruce', 'Batman'), ('Clark', 'Superman'), ('Peter', 'Spiderman'), ('Logan', 'Wolverine'), ('Wade', 'Deadpool')]
WE HAVE A LIT OF TUPLES HERE!!
'''

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict = {}
for name, hero in list(zip(names, heros)):
    my_dict[name] = hero
print(my_dict)

#>>>   {'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
print('############### ############dictionary COMPREHENSIBLE WAY  ############ ############')

my_dict = {name: hero for name, hero in list(zip (names,heros))}
print(my_dict)

'''
############### ############dictionary COMPREHENSIBLE WAY  ############ ############
{'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
'''

my_dict = {name: hero for name, hero in list(zip (names,heros)) if name != 'Peter'}
print(my_dict)
#>>> {'Bruce': 'Batman', 'Clark': 'Superman', 'Logan': 'Wolverine', 'Wade': 'Deadpool'}
# If name not equal to Peter

# Set Comprehensions: Set is a list with all unique values!!!
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
#>> {1, 2, 3, 4, 5, 6, 7, 8, 9}

print('############### ############ SET COMPREHENSIBLE WAY  ############ ############')
my_set = {n for n in nums}
print(my_set)
'''
############### ############ SET COMPREHENSIBLE WAY  ############ ############
{1, 2, 3, 4, 5, 6, 7, 8, 9}
'''


# Generator Expressions - v similar to list comprehension
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print(i)
    '''
    1
4
9
16
25
36
49
64
81
100
'''
######## OR...the comprehensible way

my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)
'''
same o/p as above
'''
