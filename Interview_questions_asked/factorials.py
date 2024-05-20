# Factorial Challenge

def factorial(num):
    if not isinstance(num, int):
        return "Please enter a whole number"
    elif num < 0:
        return "Please enter a positive number"
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)


number = -2
result = factorial(number)
print(f'The factorial of {number} is {result}')
