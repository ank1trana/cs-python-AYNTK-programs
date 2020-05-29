
#we can use the above function by importing this file directly
#all this is new separate file where importing happens

import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')
print(index)
#>>> 1

#We can also specify a name to make module name shorter
#e.g.

import my_module as mm
#that will enable us to do:

index = mm.find_index(courses, 'Physics')
print(index)
#>> 2
#how to import function itself?

from my_module import find_index
courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'CompSci')
print(index)
#>> 3

#to import both the method and the string
from my_module import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'CompSci')
print(index)
print(test)
#>>>3
#Test String

#can even name a method like:
from my_module import find_index as fi, test as t_str
courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'CompSci')
print(index)
print(t_str)
#>>>3
#Test String

#To import everything, BUT IT IS FROWNED UPON
#now we can't tell what came from theat module and what did not
#importing select stuff is better for debugging
from my_module import *

# when we import itinterpreter checks multiple locations in a list sys.path
import sys
#the following prints a list type
print(sys.path)

#>>> Test String ['/Users/ankit/Documents/GitHub/cs-python-AYNTK-programs', 
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
#  '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', 
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', 
# '/Users/ankit/Library/Python/3.8/lib/python/site-packages', 
# '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages']

# same directory as the script that is requesting import -> python path ->  std library directories, side packages or third party packages
#so we can append a new path for supporting import
sys.path.append('/Users/ankit/Documents/GitHub/cs-python-AYNTK-programs')
print(sys.path)
'''
['/Users/ankit/Documents/GitHub/cs-python-AYNTK-programs', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip', 
'/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', 
'/Users/ankit/Library/Python/3.8/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages', 
'/Users/ankit/Documents/GitHub/cs-python-AYNTK-programs']
'''
'''
One can add IT TO PYTHON PATH ENVIRONMENT VARIABLE

export PYTHONPATH="the path to the import modules" IN THE BASH FILE AS WELL.
'''
######### random module ############

import random
courses = ['H', 'M', 'C', 'R']
random_course = random.choice(courses)
print(random_course)
#>>M
import math

rads = math.radians(90)
print(rads)
print(math.sin(rads)) #rad to sine equivalent
#>> 1.5707963267948966
#>> 1.0

import datetime
import calendar

today = datetime.date.today
print(today)
print(calendar.isleap(2020))
#<built-in method today of type object at 0x10f23e4d8>
#True

import os
#gives access to underlying OS
print(os.getcwd)
#<built-in function getcwd>
print(os.getcwd())
#>>> /Users/ankit/Documents/GitHub/cs-python-AYNTK-programs

#we can scan file sys, create files, delete them etc.
#Python comes with all this stuff ready to be used as standard libraries. these modules are py files themselves.

print(os.__file__)
# this tells where this file is stored but it has to be an os attribute
#>>> /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/os.py
#print(os.dictionaries.py)
#will not work and throws:
#AttributeError: module 'os' has no attribute 'dictionaries'

