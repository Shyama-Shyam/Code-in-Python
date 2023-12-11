'''
Since everything is an object in Python programming, 
data types are actually classes and variables are instances (object) of these classes. 
The following are the standard or built-in data types in Python:
Numeric  [int , float , complex]
Sequence Type [list , tuple, string]
Boolean
Set
Dictionary
Binary Types( memoryview, bytearray, bytes)
'''

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove items and add new items.
**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
'''

#Numeric
print(f"integer {2}, {type(2)}")
print(f"float {2.7}, {type(2.7)}")
print(f"complex {3+5j}, {type(3+5j)}")
print(f"string {'abcd'}, {type('abcd')}")





#list : ordered collection of data,  items in a list do not need to be of the same type
# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
# Accessing elements
first_element = my_list[0]
print("First Element:", first_element)
last_element = my_list[-1]
print("Last Element:", last_element)

# Modifying elements
my_list[1] = 10

# Adding elements at the end
my_list.append(6)
print(my_list)
# Adding elements at a specific index
my_list.insert(2, 7)
print(my_list)
# Extending the list with another iterable
my_list.extend([8, 9, 10])
print(my_list)
# Removing elements by value
my_list.remove(3)
print(my_list)
# Removing elements by index
del my_list[0]
print(my_list)
# Popping elements by index (returns the popped value)
popped_value = my_list.pop(1)
print("Popped Value:", popped_value)
# Slicing the list
subset = my_list[1:4]
print("Subset:", subset)
# Copying a list (shallow copy)
copied_list = my_list.copy()
print("Copied List:", copied_list)
# Reversing the list in-place
my_list.reverse()
print(my_list)
# Sorting the list in-place
my_list.sort()
print(my_list)
# Finding the index of an element
index_of_5 = my_list.index(5)
print("Index of 5:", index_of_5)
# Counting occurrences of an element
count_of_5 = my_list.count(5)
print("Count of 5:", count_of_5)
# Clearing all elements from the list
my_list.clear()
print(my_list)




#TUPLE
# Tuple: ordered collection of data, items in a tuple do not need to be of the same type
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# Accessing elements
first_element = my_tuple[0]
print("First Element:", first_element)
last_element = my_tuple[-1]
print("Last Element:", last_element)

# Modifying elements is not allowed as tuples are immutable

# Adding elements is not allowed as tuples are immutable

# Combining tuples (concatenation)
combined_tuple = my_tuple + (6, 7, 8)
print("Combined Tuple:", combined_tuple)

# Multiplying a tuple
multiplied_tuple = my_tuple * 2
print("Multiplied Tuple:", multiplied_tuple)

# Counting occurrences of an element
count_of_5 = my_tuple.count(5)
print("Count of 5:", count_of_5)

# Finding the index of an element
index_of_3 = my_tuple.index(3)
print("Index of 3:", index_of_3)





#SETS
# Set: unordered collection of unique elements
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding elements
my_set.add(6)
print("After adding 6:", my_set)

# Adding multiple elements
my_set.update({7, 8, 9})
print("After updating with {7, 8, 9}:", my_set)

# Removing an element
my_set.remove(3)
print("After removing 3:", my_set)

# Removing an element (if present)
my_set.discard(4)
print("After discarding 4:", my_set)

# Pop an arbitrary element
popped_element = my_set.pop()
print("Popped Element:", popped_element)

# Clearing all elements from the set
my_set.clear()
print("After clearing:", my_set)

# Creating two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union of sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference between sets
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric difference between sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)

# Checking disjoint sets
are_disjoint = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?", are_disjoint)


#DICTIONARY
# Dictionary: unordered collection of key-value pairs
# Creating a dictionary
my_dict = {'key1': 1, 'key2': 2, 'key3': 3}
print("Original Dictionary:", my_dict)

# Accessing values by key
value_of_key1 = my_dict['key1']
print("Value of key 'key1':", value_of_key1)

# Modifying values
my_dict['key2'] = 10
print("After modifying value of 'key2':", my_dict)

# Adding a new key-value pair
my_dict['key4'] = 4
print("After adding 'key4':", my_dict)

# Removing a key-value pair
removed_value = my_dict.pop('key3')
print("Removed value of 'key3':", removed_value)
print("After removing 'key3':", my_dict)

# Removing a key-value pair (alternative)
del my_dict['key1']
print("After deleting 'key1':", my_dict)

# Clearing all key-value pairs
my_dict.clear()
print("After clearing:", my_dict)

# Creating two dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 30, 'd': 4, 'e': 5}

# Updating dictionary with another dictionary
dict1.update(dict2)
print("After updating with dict2:", dict1)

# Getting keys, values, and items
keys = dict1.keys()
values = dict1.values()
items = dict1.items()
print("Keys:", keys)
print("Values:", values)
print("Items:", items)


