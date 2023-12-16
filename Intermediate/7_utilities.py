#MAP function
# short form of list comprehension , useful when your funtion/operation is large

l = [1,2,3,4,5,6,7,8,9,10]
def func(x):
    """quadratic transformation"""
    print(x**2 + x + 1)

l_new = list(map(func, l))
print(l_new)

#FILTER:  used to construct an iterator from elements of an iterable for which a function returns true

def is_odd(x):
    return x%2==1

a = list(filter(is_odd , l))
print(a)

# COUNTERS : ount the occurrences of elements in a collection. 
#It's particularly useful for counting the frequency of elements in iterable objects like lists, strings, or other iterables
from collections import Counter
my_list = [1, 2, 3, 1, 2, 1, 4, 5]
counter_object = Counter(my_list)

# Access counts
print(counter_object)
# Output: Counter({1: 3, 2: 2, 3: 1, 4: 1, 5: 1})
# Access count of a specific element
print(counter_object[1])
# Output: 3 (because 1 occurs 3 times)
# Access the most common elements
most_common_elements = counter_object.most_common(2)
print(most_common_elements)
# Output: [(1, 3), (2, 2)]
# Create another Counter
another_list = [1, 2, 2, 3, 4]
another_counter = Counter(another_list)

# Adding Counters
combined_counter = counter_object + another_counter
print(combined_counter)
# Output: Counter({1: 4, 2: 4, 3: 2, 4: 2, 5: 1})

# Subtracting Counters
subtracted_counter = counter_object - another_counter
print(subtracted_counter)
# Output: Counter({1: 2})
