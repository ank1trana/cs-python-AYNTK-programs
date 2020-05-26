#functions.py
#instructions packaged together that perform a specific task
#def keyword - stands for definiton

def hello_func():
    pass #dont wanna do anything now but dont want errors either

hello_func() # invoking the function
print(hello_func)
#>>> <function hello_func at 0x10af894c0>

def hello_func1():
    print('Hello function')

hello_func1()
#>>> Hello function

#functions allows us to put code with specific purpose in a single location


########### return statements ##################

def returner():
    return "i am returned string"

print(returner())
#>>> i am returned string

print(len('Test'))
#>>> 4 is also a returned nu,eric value by a built in function

def returner1():
    return "i am returned string as well"

print(returner().upper())
#>>> I AM RETURNED STRING

############## working with parameters/arguments ########################
def hi_world(greeting): #takes on argument
    return f'{greeting},  my friend'
    #f strings are faster (~ twice as fast) than calling '{} my friend'.format(greeting) because it is a call to an external functions
'''
    #>>> timeit.timeit("""name = "Eric"
age = 74
 '{} is {}.'.format(name, age)""", number = 10000)
0.004242089427570761

    #>>> timeit.timeit("""name = "Eric"
 age = 74
 f'{name} is {age}.'""", number = 10000)
0.0024820892040722242
'''
print(hi_world('Hello'))

#example 2

def hi_again(greeting, name = 'Ankit'): #param given a default value
    return f'{greeting}!, {name}. hoW ARE YOU?'

print(hi_again('Hola!'))
#>>> Hola!!, Ankit. hoW ARE YOU?

#What happens if you invoke the function as:
print(hi_again('Hola!', name = 'Ranjit'))

#>>> Ranjit overwrites the default value and it prints Hola!!, Ranjit. hoW ARE YOU?

############ (*args) and (**args)

def student_info(*args, **kwargs):
    print(args) #prints a tuple
    print(kwargs) #prints a dictionary
student_info ('Math', 'Art', NAME = 'ankita', AGE =26)    
'''
('Math', 'Art')
{'NAME': 'ankita', 'AGE': 26}
'''
def student_info(*args, **kwargs):
    print(args) #prints a tuple
    print(kwargs) #prints a dictionary

courses = ['Math', 'Art']
info = {'name': 'Ankit', 'age': 27}
print('@@@@@@@@@@@@@')
#student_info ('Math', 'Art', NAME = 'ankita', AGE =26)  
student_info(courses,info)
'''
@@@@@@@@@@@@@
(['Math', 'Art'], {'name': 'Ankit', 'age': 27})
{}

* infront if list and ** in frion of dictionary will unpack them, otherwise it wont
'''
def student_info(*args, **kwargs):
    print(args) #prints a tuple
    print(kwargs) #prints a dictionary

courses = ['Math', 'Art']
info = {'name': 'Ankit', 'age': 27}
print('^^^^^^^^^^^^^^^')
#student_info ('Math', 'Art', NAME = 'ankita', AGE =26)  
student_info(*courses,**info)
'''
^^^^^^^^^^^^^^^
('Math', 'Art')
{'name': 'Ankit', 'age': 27}
'''

############# sampke snippet to put it all toghether ####################

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))
#>> Fasle
print(is_leap(2020))
#>> True
print(days_in_month(1991,11))
#>> 30
print(days_in_month(2020,2))
#>> 29