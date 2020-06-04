'''
LEGB 
Local, Enclosing, Global, Built-in
'''

'''We talk about variable scope with LEGB'''
#This is the order that the interpreter checks the scope in

x = 'global x'
#x is now a global variable as it is in the main body of our file.

def test():
    y = 'local y'
    print(y)

test() #python uses LEGB rule and finds a local var y rightaway

def test():
    y = 'local y'
    #print(y)
    print(x)

test() #is able to find x globally after failing to find one locally
'''
print(y)
Traceback (most recent call last):
  File "the_LEGB_rule.py", line 25, in <module>
    print(y)
NameError: name 'y' is not defined
BECAUSE y scope ends with the function scope
'''

print(x)
#>>>global x
#this still works coz x has global scope 
####################################################
print('fun exercise on scope')
x = 'global x'
#x is now a global variable as it is in the main body of our file.

def test():
    x = 'local x'
    print(x)

test()
print(x) 
'''
fun exercise on scope
local x
global x

because first access to local x was successful but as function ended only the global
 version remained and access to Local was lost
'''
#WE CAN EXPLICITLY TELL PYTHON TO WORK WITH GLOBAL VERSION

print('Explicit mentioning')
def test():
    global x
    x = 'local x'
    print(x)

test()
print(x) 
'''
Explicit mentioning
local x
local x
'''
####################### ARGUMENT WAS PASSED ###############

def test(z):
    x = 'local x'
    print(x) #FINDS IN THE LOCAL SCOPE

test('local z')
#print(z) will crash as it has local scope

################## tHE BUILT-IN PART #############################################

m = min([5,1,4,3,2,5,-1,11])
print(m)
#prints -1
#we can simply say 

import builtins
print(dir(builtins))
'''
'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'Connect
ionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'Fals
e', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexEr
ror', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryErr
or', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'Referenc
eError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError
', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWa
rning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 
'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict'
, 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'i
nt', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'pr
operty', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
'''

#YOU DONT WANNA ACCIDENTALLY OVERWRITING THESE BUILTINS
#e.g. crating a min function 

'''def min():
    pass
m = min([5,1,4,3,2,5,-1,11])
print(m)
'''
'''
Traceback (most recent call last):
  File "the_LEGB_rule.py", line 107, in <module>
    m = min([5,1,4,3,2,5,-1,11])
TypeError: min() takes 0 positional arguments but 1 was given

PYTHON FOUND min func in our LOCAL scope and overlooked the global scope version that actually calculates'''
#################################
#THE 'E' PART
#NESTED FUNCTIONS MOSTLY
print('*********** inner vs outer scope ***************')

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()

#we have an outer func we ran and then set a local x var (local to outer), inside our inner func we set x var which is local to out inner()
#upon printing as per LEGB, 
'''
inner x
outer x
'''
def outer():
    x = 'outer x'

    def inner():
        #x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()
'''
outer x
outer x
'''
def outer():
    x = 'outer x'

    def inner():
        #x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()
'''
should crash. think why?
'''

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()

'''
inner x
inner x

we are affecting the local copy twice

nonlocal IS USED WAY MORE OFTERN WITH CLOSURES AND DECORATORS
'''
print('THE FINAL ORDER TEST >>>>>>>>>>>>>>>>>')
x = 'global x ver'
def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()
print(x)
'''
THE FINAL ORDER TEST >>>>>>>>>>>>>>>>>
inner x
inner x
global x ver
''' 