# How to convert hex to decimal

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hexToDec(hexNum):
    hexNum = hexNum.upper()
    decNum = 0
    # This starts a loop that will iterate over each digit in hexNum in reverse order. On each iteration, i will be the
    # index of the digit (starting from 0 and increasing by 1 on each iteration), and digit will be the digit itself.
    for i, digit in enumerate(reversed(hexNum)):
        if digit not in hexNumbers:
            return "Invalid hexadecimal number"
        decNum += hexNumbers[digit] * (16 ** i)
    return decNum

print(hexToDec('A2'))  # Output: 162
print(hexToDec('random words!'))  # Output: Invalid hexadecimal number