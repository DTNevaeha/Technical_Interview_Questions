## Practicing with loops and dictionaries. To have loops read information
## from dictionaries, as well as removing values in arrays.

people = [
    {"name": "Bob", "age": 24},
    {"name": "Alice", "age": 27},
    {"name": "Geralt", "age": 33},
    {"name": "Ciri", "age": 22},
]

# Sort the list of dictionaries by the 'name' key
sorted_people = sorted(people, key=lambda x: x['name'])

# Loop through the list of dictionaries and print the name of each person
for person in sorted_people:
    print(person["name"], end=" ")  # Print all names on the same line

# Copy people then remove the last person from the list and save it to a variable
copy_people = people.copy()
remove_last = copy_people.pop()
print("\n" + str(remove_last))

# Shows that the original list has not been modified in any way.
print(people)


## Using a list of
numbers = [0, 2, 8, 6, 15, 23, 1, 109, 2, 2, 6, 8]
print(' '.join(map(str, numbers))) # This handles mixed types of data, such as int to string to print on the same line.

# Print only the first 3 values in numbers
for number in numbers[:3]:
    print(number, end=" ")

# Print all but the last 3 values in numbers
for number in numbers[-3:]:
    print(number, end=" ")

print("")
print(len(numbers)) # Prints the length of the array starting at 1 not 0

# Print only odd numbers from the array
for number in numbers:
    if number % 2 == 1:
        print(number, end=" ") # Prints all odd numbers in the array

print("")
numbers.sort() # sorts the array in ascending order
print(numbers) # show sorted array
numbers.pop(3) # Remove the 4th
print(numbers) # Show array after removing 4th

# Remove reoccuring numbers from the array
for number in numbers:
        numbers.remove(number)
print(numbers) # Show array after removing odd numbers

