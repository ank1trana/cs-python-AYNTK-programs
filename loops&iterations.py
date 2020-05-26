#for and while loops usage
nums = [1,2,3,4,5]
for num in nums:
    print(num)
'''
1
2
3
4
5
'''

#break (completely breaks out) and continue (next iter)
for num in nums:
    if num == 3:
        print('found')
        break
    print(num)
'''
1
2
found
'''
for num in nums:
    if num == 3:
        print('found')
        continue
    print(num)
'''
1
2
found
4
5
'''
################ loop within a loop ##############
for num in nums:
    for letter in 'ab':
        print(num,letter)
'''
1 a
1 b
2 a
2 b
3 a
3 b
4 a
4 b
5 a
5 b
'''
################# built in func range() ###############

for i in range(10):
    print(i)
#>> prints 0 through 9
for i in range(1,11):
    print(i)
#>> prints 1 through 10, 11 is not included 

############### WHILE LOOPS ############################ 
x =0
while x <10:
    print(x)
    x+=1
#>>> prints 0 through 9
#be cautious of infinite loops with while loops

#example of infinite loop
x =0
while True:
    #if x ==5:
    #    break
    print(x)
    x+=1
# CTRL + C helps break out of infinite loops
'''
426683
426684
426685
426686
426687
426688
426689
426690
426691
426692
^C426821
Traceback (most recent call last):
  File "loops&iterations.py", line 74, in <module>
    print(x)
KeyboardInterrupt
'''