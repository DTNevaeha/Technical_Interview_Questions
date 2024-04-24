# Ways to detect situations in which errors should be raised, and then raise them
class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise NonIntArgumentException('Non-int argument detected')
        return func(*args)
    return wrapper

# Your answer should be the largest value in the numbers list.
@handleNonIntArguments
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1, 2, 'a')
    print('This should not print out')
except NonIntArgumentException as e:
    print('Hooray!')