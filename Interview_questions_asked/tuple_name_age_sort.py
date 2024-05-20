# Create a list of tuples containing names and ages
people = [('Bob', 30), ('Alice', 25), ('Charlie', 20), ('David', 35)]

# Sort the list of tuples by age
people_sorted = sorted(people, key=lambda x: x[1])

# Convert the sorted list of tuples back to a list
people_sorted_by_age = [(name, age) for name, age in people_sorted]
# Print the sorted list by age
print(people_sorted_by_age)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30), ('David', 35)]

# print people by names
people_sorted_by_name = sorted(people, key=lambda x: x[0])
print(people_sorted_by_name)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 20), ('David', 35)]


# The sorted() function takes an optional key parameter that specifies a function to be called on each element before
# comparison. In this case, we use a lambda function to extract the second element (age) from each tuple for sorting.
# The sorted list of tuples is then converted back to a list using a list comprehension. The final sorted list is printed
# to the console.
