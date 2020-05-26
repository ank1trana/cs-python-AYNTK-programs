#key-value pairs
#called hashmaps in other languages
#key - unique identifier
#value - the data

student = {'name':'ankit', 'age':'27','courses':['Math','Java']}

print(student)
#>>> {'name': 'ankit', 'age': '27', 'courses': ['Math', 'Java']}
print(student['name']) #gives value of name key
#>>> ankit
print(student['courses'])
#>>>['Math', 'Java']
#notice it is a collection of data types in dictionaries - string, int and list in the example above
#all our keys are strings above but can be any immutable datatype
#e.g.: instead of str you could have 'name' replaced by 1 as in 1: 'ANkit' and that is fine
###############################
#using the get method

print(student.get('name'))
#will give output
#>>>ankit
print(student.get('phone'))
#will return None and NOT result in a crash. A crash happens if you use the key directly i.e. print(student['phone']) is  a NO GO .
#>>>None

#UPDATE method
student.update({'name': 'Ranjeet', 'age':50})
print(student)
{'name': 'Ranjeet', 'age': 50, 'courses': ['Math', 'Java']}
#Deletion or removal BY DEL() METHOD
del student['age']
print(student)
#>>>{'name': 'Ranjeet', 'courses': ['Math', 'Java']}

#removal by pop() method. Removes and returns the POPPED VALUE, WHICH IS V HELPFUL

name = student.pop('name')
print('popped  '+ name)
#popped  Ranjeet

################################### part 2 ############################
print('**************************************************************************')
vidyarthi = {'name':'ankit', 'age':'27','courses':['Math','Java']}
print(vidyarthi.keys())
print('**************************************************************************')
print(vidyarthi.values())
print('**************************************************************************')
print(vidyarthi.items())
print('**************************************************************************')
'''
**************************************************************************
dict_keys(['name', 'age', 'courses'])
**************************************************************************
dict_values(['ankit', '27', ['Math', 'Java']])
**************************************************************************
dict_items([('name', 'ankit'), ('age', '27'), ('courses', ['Math', 'Java'])])
**************************************************************************
'''
############################## LOOPING THROUGH ###################
print('************************* LOOP OUTPUTS *******************************')
for item in vidyarthi.items():
    print(item)

'''
('name', 'ankit')
('age', '27')
('courses', ['Math', 'Java'])
'''
for key,value in vidyarthi.items():
    print(key,value)

'''
name ankit
age 27
courses ['Math', 'Java']
'''

#Not the difference?
#The latter allows for easier access to key and values for further computation, the former prints out tuples.




