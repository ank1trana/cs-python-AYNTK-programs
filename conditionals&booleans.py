#chap 6
#true/false values are called booleans

if False:
    print('Conditional was true')
#>>> prints nothing
if True:
    print('Conditional was true')
    #>>> Conditional was true

##############################
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is (if values are the same object in memory)

language = 'Python'

if language == 'Python':
    print('Yes it is Python')
elif language == 'Java':
    print('Java it is!')
else:
    print('No match found!')
#>>> Yes it is Python
################################################
#THERE IS NO SWITCH CASE STATEMENT IN PYTHON BECAUSE IF-ELIF GIVES US THE SAME FUNCTIONALITY
################################################
# BOOLEAN OPERATIONS - and or  not
user = 'Admin'
loggedin = True

if user == 'Admin' and loggedin:
    print('Welcome Admin!')
else:
    print('bad creds!')
#>>> Welcome Admin!

#example 2 - one of the 2 evaluates to true will let it go through to admin
user = 'Admin'
loggedin = False

if user == 'Admin' or loggedin :
    print('Welcome Admin!')
else:
    print('bad creds!')
#>>> Welcome Admin!
#example 3
user = 'Admin'
loggedin = False
print('########### example 3 ###########')
if not loggedin :
    print('please log in as Admin!')
else:
    print('wilkommen!')
'''
########### example 3 ###########
please log in as Admin!
'''
###################################################### is vs ==
a = [1,2,3]
b = [1,2,3]
print(a==b)

print(id(a))
print(id(b))
print(a is b) #they are diff objects. iT WILL REMAIN FALSE UNTIL YOU DO A=B

'''
True
4379196800
4379630848
False
'''
#### Conditions that evaluate to False by default in python
# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.
############################# now we will test these below
print('########### example 4: default False conditions ###########')

condition = None
#condition = 0
#condition = 10 -> will be true
#condition = [] will be false
#condition = '' will be false
#condition = {} will be false
#condition = 'Test' --> will give True

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')






