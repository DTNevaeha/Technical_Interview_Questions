# How do I find missing numbers in a list or array?
# To find missing numbers in a list or array, you can use the following approaches:
# 1. Using a set: Convert the list to a set and then create a set of all numbers in the range from the minimum to the
    # maximum of the list. Subtract the two sets to find the missing numbers.
# 2. Using a list comprehension: Create a list of all numbers in the range from the minimum to the maximum of the list
    # that are not present in the original list.
# 3. Using a loop: Iterate over the range from the minimum to the maximum of the list and check if each number is
    # present in the list. If not, add it to a separate list of missing numbers.

# Example 1: Using a set to find missing numbers in a list
# This is a time complexity of 0(n) because it's a set and it's a constant time operation.
list1 = [1, 2, 3, 4, 6, 7, 9]
min_num = min(list1)
max_num = max(list1)
missing_nums = set(range(min_num, max_num + 1)) - set(list1)
print(list(missing_nums))  # Output: [8, 5]
# Sets in Python are unordered collections of unique elements. This means that they do not maintain the elements in 
# any specific order. When you convert a set to a list using list(), the order of elements in the resulting list is not
# guaranteed to be in any specific order.
print(sorted(list(missing_nums)))  # Output: [5, 8]

# Example 2: Using a list comprehension to find missing numbers in a list
list2 = [10, 11, 13, 14, 15]
min_num = min(list2)
max_num = max(list2)
missing_nums = [num for num in range(min_num, max_num + 1) if num not in list2]
print(missing_nums)  # Output: [12]

# Example 3: Using a loop to find missing numbers in a list
list3 = [20, 22, 23, 25]
min_num = min(list3)
max_num = max(list3)
missing_nums = []
for num in range(min_num, max_num + 1):
    if num not in list3:
        missing_nums.append(num)
print(missing_nums)  # Output: [21, 24]

