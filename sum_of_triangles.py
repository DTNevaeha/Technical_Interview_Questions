# Given a function `triangle` that returns the triangular number for a given num, create a function `square`
# that returns the square of a given positive integer, num
# A triangular number isa number, plus all the numbers below it.
# For example, triangle(4) = is a triangular number because 1 + 2 + 3 + 4 = 10

def triangle(num):
    if num < 1:
        return 0
    elif num == 1:
        return num
    else:
        return num + triangle(num - 1)

def square(num):
    return triangle(num) + triangle(num - 1)

print(square(6))  # Output: 36
print(square(4))  # Output: 16
print(square(3))  # Output: 9
print(square(37)) # Output: 1369
print(square(0))  # Output: 0
print(square(-1)) # Output: 0