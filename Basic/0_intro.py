'''
In Python, everything is an object. An object is a self-contained unit that consists of data and 
associated behaviors, known as attributes and methods. These objects are instances of classes, 
which serve as blueprints or templates defining the structure and behavior of the objects.
Here are some key points about objects in Python:

Instances of Classes:
Objects are instances of classes. A class is a user-defined data type that defines a blueprint for creating objects.
When you create an object, you are creating an instance of a particular class.

Attributes and Methods:
Objects have attributes, which are variables that store data, and methods, which are functions that operate on the data.
Attributes and methods are accessed using the dot notation: object.attribute or object.method().

Data Abstraction:
Objects provide a way to abstract and encapsulate data, allowing you to organize and structure your code in a more modular and reusable way.

Dynamic Typing:
Python is a dynamically typed language, and objects can change their type during runtime. For example, 
a variable can refer to an integer at one point and a string at another.

Built-in Objects:
Python has many built-in objects, such as integers, floats, strings, lists, dictionaries, and more. 
These built-in objects are used to represent fundamental data types.

'''


#keywords
import keyword
print(f"The list of keywords :{keyword.kwlist}")

#namespace : A namespace is a system that has a unique name for each and every object in Python
# types : builtin, global, local

# global variable
 
count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()

#scope :Scope refers to the coding region from which a particular Python object is accessible
def func():
    var = 1
    print(f'var: {var}')
func()
try:
    print(var)
except:
    print('cannot print var ')

"""
multi line comment
"""

#DocString : Python Docstrings are type of comment to show how program works. Triple Quotes in Python (“”” “””)

def helloWorld():
  # This is a docstring comment
    """ This program prints out hello world """ 
    print("Hello World")
 
 
helloWorld()



