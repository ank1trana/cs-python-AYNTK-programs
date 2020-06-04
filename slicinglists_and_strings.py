my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]
print(my_list[5])
#>>5
print(my_list[::-1])
#>>> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#from 0 through 5
print(my_list[0:6])
#we use 6 as it is not included
#>>> [0, 1, 2, 3, 4, 5]

print(my_list[3:8])
#>>> [3, 4, 5, 6, 7]
###################  MIX AND MATCH STYLES
print(my_list[-7:-2])
#>>> [3, 4, 5, 6, 7]

print(my_list[1:-2])
#>>> [1, 2, 3, 4, 5, 6, 7]

print(my_list[5:9])
#>>> [5, 6, 7, 8]
print(my_list[:])
#>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#   ########### using step size in the list elements
print(my_list[2:-1:2]) #every second value
#>>> [2, 4, 6, 8]

print(my_list[2:-1:1])
#>>> [2, 3, 4, 5, 6, 7, 8] same as not specifying a step

## doing it in reverse
print(my_list[-1:2:-1])
#start at -1, goes till 2nd index and size is -1 which means decrement
#>>> [9, 8, 7, 6, 5, 4, 3]
#note: DOESN'T PRINT '2'

print(my_list[-2:2:-1])
#>> [8, 7, 6, 5, 4, 3]
#note: DOESN'T PRINT '2'

print(my_list[-2:1:-2])
#>>> [8, 6, 4, 2] 

############# to reverse the entire list
print(my_list[::-1])
#>> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print('^^^^^^^^^^^^^^^^^^^^     STRING SLICING SAMPLES     ^^^^^^^^^^^^^^^^^^^^^^^^')

sample_url = 'http://ranaankit.com'
print (sample_url)

# Reverse the url
print(sample_url[::-1])
#>>  moc.tiknaanar//:ptth


# # Get the top level domain
print(sample_url[-4:]) 
#>> .com

# # Print the url without the http://
print(sample_url[7:])
#>>>ranaankit.com

# # Print the url without the http:// or the top level domain
print (sample_url[7:-4])
#>>> ranaankit