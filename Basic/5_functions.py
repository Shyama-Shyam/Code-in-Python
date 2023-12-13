 
'''
def function_name(parameter: data_type) -> return_type:
    """Docstring"""
    # body of the function
    return expression
'''

def func(n1: int, n2: int) -> int:
    """add two integers"""
    n3 = n1 + n2
    return n3
print(func(6,7))
print(print.__doc__)  #docstring of print function
print(func.__doc__)  

#Default argument
#Allows you to specify default values for some parameters.
#If the caller does not provide a value, the default is used.
# once we have a default argument, all the arguments to its right must also have default values.
def f_default(arg1, arg2=5 , arg3 = 7):
    print(f'default arg1 {arg1}')
    print(f'default arg2 {arg2}')
    print(f'default arg3 {arg3}')
f_default(10, 8)  # arg1=10, arg2 will be 5 (default)

#keyword arguments
#arguments are matched by the parameter names, regardless of their order.
#Allows you to specify the values using the parameter names.
def student(firstname, lastname):
    print(firstname, lastname)
student(firstname='shyama', lastname='shyam')
student(lastname='shyam', firstname='shyama')

#positional arguments
#Arguments are matched by position in the function call.
#The order and number of arguments must match the function definition.
def student(firstname, lastname):
    print(firstname, lastname)
student('shyama', 'shyam')
student('shyam', 'shyama')

# Variable-Length Positional Arguments (*args): Accepts any number of positional arguments

def sum_all(*args):
    """Calculate the sum of all passed numbers."""
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print("Sum:", result)  # Output: 15


# Variable-Length Keyword Arguments (**kwargs): Accepts any number of keyword arguments

def print_info(**kwargs):
    """Print information provided as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=25, city="New York")


# Combining *args and **kwargs in a function
def process_data(*args, **kwargs):
    """Process variable-length positional and keyword arguments."""
    print("Positional Arguments:")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
process_data(1, 2, 3, name="Alice", age=30, city="London")


#ORDER of ARGUMENTS
def example_function(positional1, positional2, default1=10, default2=20, *args, keyword1, keyword2=30, **kwargs):
    """
    This function demonstrates the order of different types of arguments.
    
    Parameters:
    - positional1, positional2: Positional arguments
    - default1, default2: Default arguments
    - *args: Variable-Length Positional Arguments
    - keyword1, keyword2: Keyword arguments
    - **kwargs: Variable-Length Keyword Arguments
    """
    print("Positional Arguments:", positional1, positional2)
    print("Default Arguments:", default1, default2)
    print("Variable-Length Positional Arguments:", args , type(args))
    print("Keyword Arguments:", keyword1, keyword2)
    print("Variable-Length Keyword Arguments:", kwargs ,type(kwargs))

# Example call
example_function(1, 2, keyword1="apple", keyword2="orange", additional_arg1=100, additional_arg2=200)

#lamda keyword is used for anonymous function
add = lambda n1, n2 : (n1+n2)
print(add('shyama ', 'shyam'))

#pass by object refernce
'''
In programming (like in Python), when we say "pass by object reference," 
it means we're not giving the actual objects to functions, but rather references or 
instructions on how to work with them. If the object is something that can be changed
 directly (like a mutable object), those changes might affect the original. 
 If it's something that can't be changed directly (like an immutable object), the original stays the same.
'''

x = [1, 2, 3]
y = 10
z  =0
def func(p,q, r):
    p[0] = 4
    p.extend([7,8])
    #reassigning value creates a new local variable p inside the function, and it no longer references the original list 
    #p = 4
    q+=1
    return p,q,r
p,q,r = func(x , y,z)
print(p,q)
print(x,y, x is p , y is q , z is r)

#pass by object refrence
a = [1,2,3]
print(a)
c1 = a.copy() #pass the value not object, Creating a new list with the same values as a
c2  = a # pass by object whatever happens with a also happen with c , Creating a reference to the same list as a
b = a
b.append(8)
print(c1 , c2)


'''
First class objects in a language are handled uniformly throughout. They may be stored in data structures,
 passed as arguments, or used in control structures. A programming language is said to support first-class 
functions if it treats functions as first-class objects. Python supports the concept of First Class functions.

Properties of first class functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
'''

print(type(func))
# output :func is object of class "function"