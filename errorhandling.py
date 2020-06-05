
try:
    f = open('requirementssss.txt') #misspelt on purpose
except Exception:
    print('File does not exist!')
else:
    pass
finally:
    pass

#often we will only use try and except
#to handle code that might throw erros or un into exceptions
'''
(base) tpg-ma-pr-06f:cs-python-AYNTK-programs ankit$ python3 errorhandling.py 
File does not exist!
'''
try:
    f = open('requirements.txt') #misspelt on purpose
    var = bad_var #now this will throw exception
except Exception:
    print('File does not exist!')
    #>>> File does not exist!
    #BUT
print('******  catching exceptions in detail  *******')    
try:
    f = open('requirementsss.txt') #misspelt on purpose
    #var = bad_var #now this will throw exception
except FileNotFoundError as e:  
    print(e)
except Exception as e:
    print(e)
#>>> Traceback (most recent call last):
'''
******  catching exceptions in detail  *******
[Errno 2] No such file or directory: 'requirementsss.txt'
'''
print('******  use of ELSE: code that runs if try block does NOT raise an exception *******')  

try:
    f = open('requirements.txt') #misspelt on purpose
    #var = bad_var #now this will throw exception
except FileNotFoundError as e:  
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
'''
output
******  use of else: code that runs if try block does NOT raise an exception *******
numpy==1.18.4
psutil==5.7.0
pytz==2020.1
'''    
''' this^ can be put in try block too but we want to be specific about what we are trying to catch here.'''
print('******  use of FINALLY : Else clause runs when no exception but finally runs no matter what happens *******')  
#good use will be to release resources that are heavy and were being used e.g. closing a database

try:
    f = open('requirements.txt') #misspelt on purpose
    #var = bad_var #now this will throw exception
except FileNotFoundError as e:  
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally block....')
    '''
    ******  use of FINALLY : Else clause runs when no exception but finally runs no matter what happens *******
numpy==1.18.4
psutil==5.7.0
pytz==2020.1

Executing finally block....
'''
#we can raise exceptions on our own as well
print('RAISING EXCEPTIONS WHEN NEEDED')
try:
    f = open('currupt_file.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print('First!')
except Exception as e:
    print('manually raised ONE')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')
'''
RAISING EXCEPTIONS WHEN NEEDED
manually raised ONE
Executing Finally...
End of program
'''



