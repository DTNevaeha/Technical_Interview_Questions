# Create a list of tuples containing names and ages
people = [('Alice', 25), ('Bob', 30), ('Charlie', 20), ('David', 35)]

# Sort the list of tuples by age
people_sorted = sorted(people, key=lambda x: x[1])

# Convert the sorted list of tuples back to a list
people_sorted_list = [(name, age) for name, age in people_sorted]

# Print the sorted list
print(people_sorted_list)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30), ('David', 35)]

