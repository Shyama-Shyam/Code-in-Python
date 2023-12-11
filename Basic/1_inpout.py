import sys
 
sys.stdout.write("Code-IN-Python ")

#formatting
print(f"float : {987.654:.2f}") 
print(f"expo : {564.00987:.3E}") 

dictionary = dict(k1= 1, k2= 2)
print("k1 {k1} k2 {k2}".format(**dictionary))

message = "coding for now"
 
# Printing the center aligned string with fillchr
print("Center aligned string with fillchr: ")
print(message.center(40, '#'))
print(message.ljust(40, '-'))
print(message.rjust(40, '-'))

#input :This function first takes the input from the user and converts it into a string. 
#The type of the returned object always will be <class ‘str’>

val = input("Enter your value: ")
print(val , type(val))

num = int(input("Enter a number: "))
print(num, " ", type(num))
           
floatNum = float(input("Enter a decimal number: "))
print(floatNum, " ", type(floatNum))

#CONSOLE / SHELL :command line interpreter that takes input from the user i.e one command at a time and interprets it

#multiple inputs
a, b = input("Enter two values: ").split() 
print(a,b)

x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x) 

