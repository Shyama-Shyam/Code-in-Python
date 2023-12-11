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



