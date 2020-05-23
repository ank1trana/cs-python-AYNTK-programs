############################## LISTS  ########################

courses = ['history', 'math', 'comp sci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[2])
print(courses[-1])

'''
(base) ankit@Jarvis GitHub % python3 ./cs-python-AYNTK-programs/lists_tuples_sets.py 
['history', 'math', 'comp sci']
3
history
comp sci
comp sci
'''
print(courses[0:2])
#>>>['history', 'math']
print(courses[1:])
#>>>['math', 'comp sci']
############################## LIST methods available  ########################
#### add item to list

courses.append('Art')
#insert at a location
courses.insert(0,'Econ') #specified location as well, here at beginning
print(courses)
#>>>['Econ', 'history', 'math', 'comp sci', 'Art']

courses_2 = ['physc', 'political sci']
courses.insert(0,courses_2)
print(courses)
#>>> [['physc', 'political sci'], 'Econ', 'history', 'math', 'comp sci', 'Art']
#it gave us the list embedded as one element of the parent list.
#append() does the same but at the tail end
#to have it as separate lements we use Extend function

courses_new = ['Econ', 'history', 'math', 'comp sci', 'Art']
courses_new.extend(courses_2)
print(courses_new)
#>>>  ['Econ', 'history', 'math', 'comp sci', 'Art', 'physc', 'political sci']
############################## LIST removal of elements  ########################
courses_new.remove('Art')
print(courses_new)
#>>> ['Econ', 'history', 'math', 'comp sci', 'physc', 'political sci']

#pop func - treat as a stack or queue, removes only the top element
popped = courses_new.pop()
print(courses_new)
print('removed- '+ popped)
#>>>> ['Econ', 'history', 'math', 'comp sci', 'physc']
#removed- political sci

################# LIST REVERSAL, sort alphabetically ###########
print('original list')
print(courses_new)
print('reversed is:')
courses_new.reverse()
print(courses_new)
print('sorted is:')
courses_new.sort()
print(courses_new)

nums = [1,5,6,7,23,7,34,523,423,23,42,34,9]
nums.sort()
print('sorted nums is:')
print(nums)

print('decending order is:')
nums.sort(reverse=True)
print(nums)

'''
original list
['Econ', 'history', 'math', 'comp sci', 'physc']
reversed is:
['physc', 'comp sci', 'math', 'history', 'Econ']
sorted is:
['Econ', 'comp sci', 'history', 'math', 'physc']
sorted nums is:
[1, 5, 6, 7, 7, 9, 23, 23, 34, 34, 42, 423, 523]
decending order is:
[523, 423, 42, 34, 34, 23, 23, 9, 7, 7, 6, 5, 1]
'''

############ key alternative - instead of calling the sort() on the list,
#  we can use built in Sorted() but it returns a copy of sorted version, note!!
print('nums is:')
print(nums)
sorted_list = sorted(nums)
print(sorted_list)
'''
nums is:
[523, 423, 42, 34, 34, 23, 23, 9, 7, 7, 6, 5, 1]
[1, 5, 6, 7, 7, 9, 23, 23, 34, 34, 42, 423, 523]
'''

############## min max and sum ###########

print(min(nums))
print(max(nums))
print(sum(nums))
'''
1
523
1137
'''
############## LOCATING INDEX OF AN ELEMENT ###########
print(courses_new.index('history'))
#print(courses_new.index('geography'))
'''
2
Traceback (most recent call last):
  File "./cs-python-AYNTK-programs/lists_tuples_sets.py", line 111, in <module>
    print(courses_new.index('geography'))
ValueError: 'geography' is not in list
'''

#so we check if element is there using 'in'
print('geography' in courses_new)
#>>> False

###### use of enumerate to number the items

for index, course in enumerate(courses_new, start=1):
    print(str(index) +' - '+ str(course))

'''
1 - Econ
2 - comp sci
3 - history
4 - math
5 - physc
'''
### turn list into strings separated by a value - JOIN method

course_str = ', '.join(courses_new) #, as separator
print(course_str)
#>>> Econ, comp sci, history, math, physc

#########################split based on the marker ######################

new_list = course_str.split(',')
print(new_list)
#>>>> ['Econ', 'comp sci', 'history', 'math', 'physc']
new_list = course_str.split(',')
print(new_list)
#>>> ['Econ', ' comp sci', ' history', ' math', ' physc']  #note the space

######################################## tuples ############################################################

#Immutable, unlike mutable lists
# Mutable
print('######################################################')
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)
'''
######################################################
['History', 'Math', 'Physics', 'CompSci']
['History', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']

Here the change in one list object has changed the other one to because of the assignment operator.
This is called being mutable.
'''
print('************************')
# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)
'''
######################################################
['History', 'Math', 'Physics', 'CompSci']
['History', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']
['Art', 'Math', 'Physics', 'CompSci']
************************
('History', 'Math', 'Physics', 'CompSci')
('History', 'Math', 'Physics', 'CompSci')
Traceback (most recent call last):
  File "./cs-python-AYNTK-programs/lists_tuples_sets.py", line 184, in <module>
    tuple_1[0] = 'Art'
TypeError: 'tuple' object does not support item assignment

This is called being immutable, tuple object can't be assigned the new va
Also, append, remove() those methods do not work on tuples
'''

#####################   SETS vs DICTIONARY ##################################
'''
Set:

A Python set is a slightly different concept from a list or a tuple. A set, in Python,
 is just like the mathematical set. It does not hold duplicate values and is unordered.
  However, it is not immutable, unlike a tuple.

Let’s first declare a set. Use curly braces for the same.

>>> myset={3,1,2}
>>> myset
{1, 2, 3}

As you can see, it rearranged the elements in ascending order.

Since a set is unordered, there is no way we can use indexing to access or delete
 its elements. Then, to perform operations on it, Python provides us with a list of functions 
 and methods like discard(), pop(), clear(), remove(), add(), and more. Functions like len() and max() also apply on sets.

 Dictionary:

 Dictionaries are unordered sets. But the main difference is that items in dictionaries are accessed 
 via keys and not via their position. The values of a dictionary can be any Python data type. 
 A set is a collection which is unordered and unindexed. So dictionaries are unordered key-value-pairs.
'''


