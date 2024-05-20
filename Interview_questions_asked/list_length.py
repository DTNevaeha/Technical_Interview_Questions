# Implement list length
# Implement a function that returns the length of a list without using the len() function. You can iterate over the list
# and count the number of elements, or use other creative solutions.
# Time complexity: O(n)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(list1))  # Output: 10

def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# Test cases
print(list_length([1, 2, 3, 4, 5]))  # Output: 5
print(list_length([]))  # Output: 0
print(list_length(['a', 'b', 'c', 'd']))  # Output: 4
print(list_length([6]))  # Output: 1

# The time complexity of this function is O(n) because it iterates over the entire list to count the number of elements.
# The function initializes a count variable to 0 and then increments it for each element in the list. The final count is
# returned as the length of the list. This approach is a simple and straightforward way to calculate the length of a list
# without using the len() function.

# Another approach to calculate the length of a list without using the len() function is to use a while loop to iterate
# over the list and increment a counter until the end of the list is reached. This approach is similar to the previous
# solution but uses a while loop instead of a for loop.

def list_length(lst):
    count = 0
    while lst:
        count += 1
        lst = lst[1:]
    return count

# Test cases
print(list_length([1, 2, 3, 4, 5]))  # Output: 5
print(list_length([]))  # Output: 0
print(list_length(['a', 'b', 'c', 'd']))  # Output: 4
print(list_length([6]))  # Output: 1

# This approach also has a time complexity of O(n) because it iterates over the entire list using a while loop to count
# the number of elements. The while loop continues until the list is empty, and the counter is incremented for each
# iteration. The final count is returned as the length of the list. This approach is another way to calculate the length
# of a list without using the len() function.

# Another approach to calculate the length of a list without using the len() function is to use a recursive function that
# counts the number of elements in the list. The recursive function takes the list as input and checks if the list is
# empty. If the list is empty, the function returns 0. Otherwise, it increments the count by 1 and recursively calls

def list_length(lst):
    if not lst:
        return 0
    return 1 + list_length(lst[1:])  # Recursive call with the rest of the list

# Test cases
print(list_length([1, 2, 3, 4, 5]))  # Output: 5
print(list_length([]))  # Output: 0
print(list_length(['a', 'b', 'c', 'd']))  # Output: 4
print(list_length([6]))  # Output: 1
