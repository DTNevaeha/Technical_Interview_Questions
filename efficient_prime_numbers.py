# How to efficiently calculate for prime numbers
# Example: I want to check if the number 51 is a prime
# Inefficient method: Test to see if 51 is divisible by any number from 2, 3, 4, 5, 6, 7, 8
# Efficient method: Test to see if 51 is divisible by any number from 2, 3, 5, 7

def allPrimesUpTo(num):
    numList = [True] * (num + 1)
    for x in range(2, int(num**0.5) + 1):
        if numList[x]:
            for i in range(x*x, num + 1, x):
                numList[i] = False
    return [x for x in range(2, num) if numList[x]]

num = 100 # Check for all prime numbers up to 100
result = allPrimesUpTo(num)
print(result)

# Gives back true or false if a number is a prime number
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(isPrime(51)) # False
print(isPrime(53)) # True
print(isPrime(2)) # True
print(isPrime(1)) # False
print(isPrime(0)) # False
