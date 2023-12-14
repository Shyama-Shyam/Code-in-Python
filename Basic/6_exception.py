'''
2 type of errors in python
Syntax errors : occur when the Python interpreter encounters code that violates the language's syntax rules. 
These errors are typically detected during the parsing (compilation) phase.

Runtime errors / Exceptions : occur during the execution of a program. 
These errors are not detected during the parsing phase but rather when the program is running.

common errors:
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.
'''
l = [1,2,3,4]
try:
    l[8]+=0
except:
    print("an error ocured")

#catching specific exception
def fun(a):
    if a < 4:
 
        b = a/(a-3)
    print("Value of b = ", b)
     
try:
    #fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")


#using else
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except Exception as e:
        print ("a/b result in 0", e)
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#user defined exception
# class MyError is derived from super class Exception
class MyError(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
 
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
 
 
try:
    raise(MyError(3*2))
 
# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occurred: ', error.value)

#short printing error message
name = input()
if len(name) >10:
    raise Exception("too long name try different")
else:
    print("that was a good name")

