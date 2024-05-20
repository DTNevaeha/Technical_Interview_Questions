# What are functions and data types in Python?
# Functions in Python are blocks of reusable code that perform a specific task. They can take input arguments, perform
# operations, and return output values. Functions help in organizing code, making it more readable, and reducing code
# duplication. 

##### FUNCTIONS #####
#Python provides built-in functions like print(), len(), and range(), as well as the ability to define
# custom functions using the def keyword.

##### DATA TYPES #####
# Data types in Python represent the type or category of data that a variable can hold. Python has several built-in data
# types, including:
# 1. Numeric types: int, float, complex
# 2. Sequence types: list, tuple, range
# 3. Text type: str
# 4. Mapping type: dict
# 5. Set types: set, frozenset
# 6. Boolean type: bool
# 7. Binary types: bytes, bytearray, memoryview
# Each data type has specific properties and methods associated with it, allowing you to perform different operations
# on the data. Understanding data types is essential for writing efficient and bug-free Python code.

# Example: Using functions and data types in Python
# Define a function to calculate the area of a circle
def calculate_area(radius):
    return 3.14159 * radius ** 2

# Calculate the area of a circle with radius 5
radius = 5
area = calculate_area(radius)
print(area)  # Output: 78.53975


# Define a function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

string1 = "Hello, World!"
reverse = reverse_string(string1)
print(reverse)  # Output: !dlroW ,olleH