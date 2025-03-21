"""
Convert an integer to a Roman numeral.
"""


def intToRoman(number: int) -> str:
    conversions = [
        [1000, "M"],
        [900, "CM"],
        [500, "D"],
        [400, "CD"],
        [100, "C"],
        [90, "XC"],
        [50, "L"],
        [40, "XL"],
        [10, "X"],
        [9, "IX"],
        [5, "V"],
        [4, "IV"],
        [1, "I"],
    ]
    result: str = ""

    for value in range(len(conversions)):
        while number >= conversions[value][0]:
            result += conversions[value][1]
            number -= conversions[value][0]

    return result


print(intToRoman(3749))  # output: "MMMDCCXLIX"
print(intToRoman(58))  # output: "LVIII"
print(intToRoman(1994))  # output: "MCMXCIV"
