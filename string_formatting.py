#beyond basics with formatting the strings!
#string formatting for Dicts, Lists, numbers and Dates

person = {'name': 'Jenn', 'age': 23}
#this  below is not very readable, you need casting of data types often, need to be careful with '

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

#THE FORMATTING OPTION
#PASSES VALUES TO PLACEHOLDERS IN ORDER
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)

#WE CAN ALSO NUMBER OUR PLACEHOLDERS
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)
#THIS^ IS USEFUL WHEN VALUES ARE TO BE REPEATDLY USED, SEE EXAMPLE BELOW

tag = 'h1'
text = 'This is a headline'
#Following builds HTML
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
#>>>   <h1>This is a headline</h1>


print('############# when passing elements of dictionary ############')
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)

print('############# equivalent way to do the above from within the placeholders ############')
sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
print(sentence)

print('############# passing dictionary once so only using [0] ############')
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

print('############# using only indices  of a list############')

l = ['ankit',29]
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)
#My name is ankit and I am 29 years old.
#the above won't work on a dictionary
print(sentence)

#FORMATTING WITH CLASSES

class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('rANJEET', '33') #INSTANCE CREATED
#USE OD DOT ATTRIBUTE TO GRAB VALUES
#VALUES PASSED IN FORMAT
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)
#>>>   My name is rANJEET and I am 33 years old.

#USE THE FOLLOWING TO PRINT DICTIONARIES. MORE READABLE  
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
print(sentence)
#>> My name is Jenn and I am 30 years old.
person = {'name': 'Kanika', 'age':24}

# the most convenient way!!
#we unpack the dict using **
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)
#>> My name is Kanika and I am 24 years old.
# FORMATTING AND PRINTING OUT NUMBERS

for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i) #ZERO PAD MY DIGITS TO 2
    print(sentence)
'''
The value is 01
The value is 02
The value is 03
The value is 04
The value is 05
The value is 06
The value is 07
The value is 08
The value is 09
The value is 10
'''
#LETS PRINT PI UPTO 2 DECIMAL PLACES
pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)
#>>   Pi is equal to 3.14

#comma separated values and also upto 2 decimal places
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)

print(sentence)
#>>  MB is equal to 1,000,000.00 bytes

import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)
#>> 2016-09-24 12:30:45

#but we want the format below
# March 01, 2016
#refer oyton documentation for formatting options 
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)
#>> September 24, 2016

#let's try and make something like the sentence below
# March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%J} day of the year'.format(my_date)
#USING 0 MEANS USE THE FIRST VALUE PASSED TO FORMAT() to obtain these
print(sentence)
#>>  September 24, 2016 fell on a Saturday and was the J day of the year