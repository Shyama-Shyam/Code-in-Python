#operators : Operators in general are used to perform operations on values and variables
'''
Types of Operators in Python
Arithmetic Operators
Comparison Operators
Logical Operators
Bitwise Operators
Assignment Operators
Identity Operators and Membership Operators
'''

#airthmetic
a , b = 1,2
add = a + b
sub = a - b 
mul = a * b
div = a/b
mod = a % b
qou = a//b
exp = a ** b

#comparison relational : It either returns True or False according to the condition
greaterthan = a>b
lessthan = a<b
equalto = a==b
notequal = a!=b
gethan = a>=b
lethan = a<=b

#logical : not>and >or 
a,b = True , False
print(a and b)
print(a or b)
print(not a)

#bitwise : act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
#AND
a = 5    # binary: 0b0101
b = 3    # binary: 0b0011
result = a & b
print(result)  # Output: 1 (binary: 0b0001)

#OR
result = a | b
print(result)  # Output: 7 (binary: 0b0111)

#XOR
result = a ^ b
print(result)  # Output: 6 (binary: 0b0110)

#NOT
result = ~a
print(result)  # Output: -6 (binary: -0b0110)

#LEFT SHIFT
result = a << 2
print(result)  # Output: 20 (binary: 0b10100)

#Assignment operators
x = 5
x += 3
x -= 2
x *= 4
x /= 3
x //= 2
x %= 3
x **= 3

a = 0b1101
a &= 0b1011
a |= 0b1011
a ^= 0b1011
a <<= 2
a >>= 2

#Identity operators :used to compare the memory locations of two objects, checking if they refer to the same object
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # Output: False (a and b are different objects)
print(a is c)  # Output: True (a and c point to the same object)

x = "hello"
y = "world"
z = x

print(x is not y)  # Output: True (x and y are different objects)
print(x is not z)  # Output: False (x and z point to the same object)


#Membership operators
l = [1,2,3,4]
print(1 not in l)
print(10 in l)



# OPERATOR OVERLOADING
# extended meaning beyond their predefined operational meaning
#same built-in operator or function shows different behavior for objects of different classes, this is called Operator Overloading

"""
Consider that we have two objects which are a physical representation of a class 
(user-defined data type) and we have to add two objects with binary + operator it throws an error, 
because compiler dont know how to add two objects. So we define a method for an operator and that process is called operator overloading
"""

'''
Python provides some special function or magic function that is automatically invoked 
when it is associated with that particular operator. For example, when we use + operator, 
the magic method __add__ is automatically invoked in which the operation for + operator is defined.
'''

class new_data_type():
    def __init__(self, n):
        self.n = n

    def __add__(self,x):
        return self.n*x.n

var1 = new_data_type(5)
var2 = new_data_type(4)
print(f"var1 + var2 ={var1+var2}")


"""
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)
-=	__isub__(self, other)
+=	__iadd__(self, other)
*=	__imul__(self, other)
/=	__idiv__(self, other)
//=	__ifloordiv__(self, other)
%=	__imod__(self, other)
**=	__ipow__(self, other)
>>=	__irshift__(self, other)
<<=	__ilshift__(self, other)
&=	__iand__(self, other)
|=	__ior__(self, other)
^=	__ixor__(self, other)


–	__neg__(self)
+	__pos__(self)
~	__invert__(self)


"""



