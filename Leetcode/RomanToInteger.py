"""
Given a roman numeral, convert it to an integer.
I             1
IV            4
V             5
IX            9
X             10
XL            40
L             50
XC            90
C             100
CD            400
D             500
CM            900
M             1000
"""


def romanToInt(numerals: str) -> int:
    numerals = (
        numerals.replace("IV", "IIII")
        .replace("IX", "VIIII")
        .replace("XL", "XXXX")
        .replace("XC", "LXXXX")
        .replace("CD", "CCCC")
        .replace("CM", "DCCCC")
    )
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for numeral in numerals:
        result += roman_numerals[numeral]
    return result


print(romanToInt("III"))  # output: 3
print(romanToInt("LVIII"))  # output: 58
print(romanToInt("MCMXCIV"))  # output: 1994
