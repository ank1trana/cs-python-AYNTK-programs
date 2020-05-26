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

