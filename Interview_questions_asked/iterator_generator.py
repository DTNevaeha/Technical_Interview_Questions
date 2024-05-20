# What is an iterator and generator
# An iterator is an object that represents a stream of data. It implements the iterator protocol, which consists of two
# methods: __iter__() and __next__(). The __iter__() method returns the iterator object itself, while the __next__()
# method returns the next element in the stream. When all elements have been exhausted, the __next__() method raises a
# StopIteration exception. Iterators can be created using iter() and next() functions.

# Example: Creating an iterator
# This is a time complexity of 0(1) because it's a constant time operation.
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Create an iterator object
my_iter = MyIterator([1, 2, 3, 4, 5])

# Iterate over the elements using next()
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 5
# print(next(my_iter))  # Raises StopIteration exception

# Generators are a special type of iterator that can be created using generator functions or generator expressions.
# Generator functions are defined using the yield keyword, which allows them to yield values one at a time. Generator
# expressions are similar to list comprehensions, but they use parentheses () instead of square brackets [].

# Example: Creating a generator function
# This is a time complexity of 0(1) because it's a constant time operation.
def my_generator(data):
    for value in data:
        yield value

# Create a generator object
my_gen = my_generator([1, 2, 3, 4, 5])

# Iterate over the elements using next()
print(next(my_gen))  # Output: 1
print(next(my_gen))  # Output: 2
print(next(my_gen))  # Output: 3
print(next(my_gen))  # Output: 4
print(next(my_gen))  # Output: 5
# print(next(my_gen))  # Raises StopIteration exception

# Generators are more memory-efficient than lists because they generate values on-the-fly rather than storing them in
# memory. They are particularly useful for processing large datasets or infinite sequences.

