li = [9,1,3,4,2,9,6,4,6,12,123,42,3]
s_li = sorted(li)
print(s_li)
#>>  [1, 2, 3, 3, 4, 4, 6, 6, 9, 9, 12, 42, 123]
print(li)
#>> [9, 1, 3, 4, 2, 9, 6, 4, 6, 12, 123, 42, 3]

# SORT WITHOUT CREATING NEW VAR

print('Directly sorting the list \t',li.sort())
# Directly sorting the list        None
#NOTE: sort() will not return a list but only compute it. It always returns None
#sort() allows modifying it in place
#sorted() allows passing any iterable sort() does not
#tuple does not have sort()

rev = sorted(li, reverse=True)
print(rev)
#>>> [123, 42, 12, 9, 9, 6, 6, 4, 4, 3, 3, 2, 1]

tup = (9 ,4 ,2 ,1 ,4,7,2,11,123, 234,6)
s_tup = sorted(tup)
print(s_tup)
#[1, 2, 2, 4, 4, 6, 7, 9, 11, 123, 234]

di = {'name': 'ANKIT', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print(s_di)
#['age', 'job', 'name', 'os']
#only the keys are sorted and returns a list with sorted keys as seen above

#SORT BASED ON A DIFF CRITERIA
#LIST OF INTEGERS SORT BASED ON THEIR ABSOLUTE VALUES

li = [-6,-5,-4,1,2,5,7,11,3]
s_li_1 = sorted(li)
print(s_li_1)
#>>> [-6, -5, -4, 1, 2, 3, 5, 7, 11]
li = [-6,-5,-4,1,2,5,7,11,3]
s_li_1 = sorted(li, key=abs)
print(s_li_1)
#>>> [1, 2, 3, -4, -5, 5, -6, 7, 11]
#key is useful when sorting named attributes
#key takes a function which takes each element of our list and processes it.

#for a class handling employee info, we can have something like:

def e_sort(emp):
    return emp.age # to return based on age in ascending order

s_employees = sorted(employees,key=e_sort, reverse=False)
print(s_employees)

#OR using lambda - a quick anonymous function
s_employees = sorted(employees,key=lambda e: e.age)
print(employees)
#OR using attrgettr

from operator import attrgetter

s_employees = sorted(employees,key=attrgetter('age'))
print(employees)


