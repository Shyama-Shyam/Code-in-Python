'''
Generators in Python are a powerful and memory-efficient way to create iterators.
 An iterator is an object that represents a stream of data and allows you to iterate over that data.
   Generators are particularly useful when dealing with large datasets or 
   when you want to generate values on-the-fly without storing them in memory.
'''

#Generators are made using functions, and instead of return, they use yield. 
# #When the function hits yield, it pauses, remembers where it stopped, and gives you the current value
def counter_generator():
    count = 0
    while True:
        yield count
        count += 1
counter_gen = counter_generator()


print(type(counter_gen))
#object of class generator not function


#Generators remember where they left off. If a generator has a loop and a yield inside it, it can keep track of its count or anything else.
for idx,  value in enumerate(counter_gen):
    print(value , end = ' ')
    if idx==5:
        break
print(next(counter_gen))  
print(next(counter_gen)) 


#create generators like list comprehension
squares = (x*x for x in range(10))
print(type(squares))



#Example : fibonacci numbers

# Traditional approach
def generate_fibonacci_list(n):
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n:
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)
    return fibonacci_list

# Using the function to generate the first 10 Fibonacci numbers
fibonacci_numbers = generate_fibonacci_list(10)
print(fibonacci_numbers)

#new approaach
def generate_fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Using the generator to generate the first 10 Fibonacci numbers
fibonacci_generator = generate_fibonacci_generator(10)
for num in fibonacci_generator:
    print(num, end = " ")






