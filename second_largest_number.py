# How to find the second largest number in a list?

# To find the second largest number in a list, you can use the following approach:
# 1. Sort the list in descending order using the sort() method or the sorted() function.
# 2. Return the second element from the sorted list.

# Example: Finding the second largest number in a list
# This is a time complexity of 0(n log n) because it's a sorting operation.
list1 = [10, 5, 20, 8, 15]
list1.sort(reverse=True)
second_largest = list1[1]
print(second_largest)  # Output: 15

# Another method to find the second largest number in a list is to iterate over the list and keep track of the two largest
# numbers encountered so far. This approach avoids sorting the entire list and is more efficient for large lists.

# Example: Finding the second largest number in a list without sorting
# This is a time complexity of 0(n) because it's a linear time operation.
list2 = [10, 5, 20, 8, 15]
largest = second_largest = float('-inf')
for num in list2:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)  # Output: 15

