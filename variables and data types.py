#variables and data types.py
message = "Hello world"
my_message = "hi friend!"
second_msg = 'okay sure'

third = 'Ankit\'s world'  

multi_line = """
first line
second line
third line
fourth line
ends here
"""
multi_line_2 = '''
pehla
doosra
teesra
chautha
paanchwa
last
'''
#Note THE USE OF Back slash above

#these 4 variables hold strings
print(message)
print(my_message)
print(second_msg)
print(third)
print('****************************************************************************')
print(multi_line)
print('****************************************************************************')
print(multi_line_2)
#single quote vs double quote?
#No differnece really except when an apostrophe is needed , use double outside and vice versa

#HOW MANY CHARACTERS IN OIUR STRING?
print(message)
print(len(message))
print('10th char is:'+  message[9])
###############################################
print(message[0:5])
#this is called slicing
#this implies from 0th character to the 4th one, not including the 5th or upperbound limit.
#alternate: [:5]
#to grab 'world' we use [6:]
###############################################
#print('11th char exists?:'+  message[11]) 
#above gives error coz that char does not exist
#print('****************************************************************************')
#print(my_message)
#print(len(my_message))

###############################################
#COnvert to lowercase
print(message.lower())
#we called an inbuilt function here
###############################################
#COnvert to uppercase
print(message.upper())
###############################################
#Count the occurence of a string or character
#using: count()
print(message.count('hello'))
#prints 0 coz case did not match
print(message.count('l'))
#prints 3
###############################################
#FIND INDEX OF A WORD IN THE TEXT CONTENT
#find()
print(message.find('world'))
#prints 6
print(message.find('Earth'))
#prints -1 meaning a fail in find
print(message.find('l'))
#prints 2, the first occurence of l out of all the 3 present
###############################################
#REPLACING A STRING WITH ANOTHER IN TEXT
# WE MUST USE A NEW VARIABLE TO STORE THE REPLACEMENT, AS the inbuilt function creates a copy of the replacement and does not alter the original string
print(message)
new_msg = message.replace('Hello','Namaste!')
#you could set it to message itself to overwrite it.
print(new_msg)
###############################################
#CONCATENATE STRINGS
#USE OF +
name = 'Ankit'
msg = 'Hi'

#combined = msg + ", " + name + ". How are you?"
combined = '{}, {}. How are you?'.format( msg , name )
print(combined)






