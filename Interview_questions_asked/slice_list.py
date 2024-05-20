# What is slicing?
# Slicing is a way to extract a subsequence from a list.
# Syntax: list_name[start:stop:step]
# start: The starting index of the slice. If not given, the default is 0.
# stop: The ending index of the slice. The slice goes up to, but does not include, the element at this index. If not given, the default is the length of the list.
# step: The amount by which the index increases. If not given, the default is 1.
# If the step is negative, the slice is taken in reverse order.
# If the start is greater than the stop, the slice will be empty.
# If the start and stop are both omitted, the slice will be a copy of the list.
# If the step is negative, the start and stop are swapped.


# What is the difference between a list and a tuple?
# A list is an ordered collection of elements enclosed in square brackets [].
# Lists are mutable, meaning their elements can be changed or modified.
# Lists can contain elements of different data types.
# Lists are commonly used to store related pieces of information together.
# Lists are slower than tuples when it comes to iteration and accessing elements.
# Lists cannot be used as keys in dictionaries.


# THESE ARE LISTS
# The time complexity of list slicing is O(k) where k is the number of elements in the slice.
# Example 1: Extracting a subsequence from a list
list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(list_nums[2:5])  # Output: [3, 4, 5]
print(list_nums[0:5:2])  # Output: [1, 3, 5]
print(list_nums[:5])  # Output: [1, 2, 3, 4, 5]
print(list_nums[5:])  # Output: [6, 7, 8, 9, 10]
print(list_nums[:])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_nums[::-1])  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list_nums[5:2:-1])  # Output: [6, 5, 4]
print(list_nums[5:2])  # Output: []

# What is a tuple?
# A tuple is an ordered collection of elements enclosed in parentheses ().
# Tuples are similar to lists but are immutable, meaning their elements cannot be changed or modified.
# Tuples can contain elements of different data types.
# Tuples are commonly used to store related pieces of information together.
# Tuples are faster than lists when it comes to iteration and accessing elements.
# Tuples can be used as keys in dictionaries, while lists cannot.
# Example: Creating a tuple

# THESE ARE TUPLES
# This is time complexity 0(1) because it's a tuple / means it takes a constant amount of time regardless of size.
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('apple', 'banana', 'cherry')
tuple3 = (1, 'apple', True)
# Accessing elements of a tuple
print(tuple1[0])  # Output: 1
print(tuple2[2])  # Output: cherry
# Tuple unpacking
a, b, *c = tuple1
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: [3, 4, 5]
# Iterating over a tuple
for item in tuple2:
    print(item) # Output: apple, banana, cherry

# Tuple methods
# Tuples have only two built-in methods: count() and index().
# count(): Returns the number of times a specified value occurs in the tuple.
# index(): Returns the index of the first occurrence of a specified value.
# Example: Using tuple methods
tuple4 = (1, 2, 3, 4, 2, 5, 2)
print(tuple4.count(2))  # Output: 3
print(tuple4.index(4))  # Output: 3 (prints the index of the first occurrence of 4)
