#Integers whole num vs float decimal
num =3
print(type(num))
print(3-2)
#in python3 is will give right answer 1.5, python2 drops the decimal
print(3/2) 
'''
(base) ankit@Jarvis GitHub % python ./cs-python-AYNTK-programs/numeric_datatypes.py
<type 'int'>
1
1
(base) ankit@Jarvis GitHub % python3 ./cs-python-AYNTK-programs/numeric_datatypes.py
<class 'int'>
1
1.5
(base) ankit@Jarvis GitHub % 
'''
######################################################################################################
print(3//2)
print(3**2)
'''
(base) ankit@Jarvis GitHub % python3 ./cs-python-AYNTK-programs/numeric_datatypes.py
1
9
'''
##################### ORDER OF OPERATIONS #####################
print(3*2+1)
print(3*(2+1))
'''
7
9
'''
##################### built in func for numerics #####################

print(abs(-2))
print(round(3.75))
print(round(3.75,1)) #upto this digit after decimal
'''
2
4
3.8
'''
##################### comparisons that return Booleans #####################
num1 = 3
num2 = 2

print(num1 == num2)
print(num1 > num2)
print(num1 != num2)
print(num1 >= num2)
'''
False
True
True
True
'''
##################### CASTING #####################'

n1 = '100'
N2 = '200'
print(n1 +N2)

n1 = int(n1)
N2 =int(N2)
print(n1 +N2)

'''
100200
300
'''

