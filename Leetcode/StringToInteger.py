'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
Whitespace: Ignore any leading whitespace
Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Read the integer by skipping leading zeros until a non-digit character is encountered
If no digits were read, then the result is 0.
If integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
'''

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        replacedString = ""
        for character in s:
            if character == " " and replacedString != "":
                if replacedString == "-" or replacedString == "+":
                    break
                return int(replacedString)
            if character.isalpha() or character == ".":
                if replacedString == "" or replacedString == "-" or replacedString == "+":
                    return 0
                break
            if character in ["-", "+"] and replacedString != "":
                if replacedString == "-" or replacedString == "+":
                    return 0
                break
            if character.isnumeric() or (character in ["-", "+"] and replacedString == ""):
                replacedString += character

        if replacedString == "" or replacedString == "-" or replacedString == "+" or replacedString.isalpha():
            return 0

        result = int(replacedString)

        # Check for the lower and upper bounds of the 32-bit signed integer
        lower_bound = -2**31
        upper_bound = 2**31 - 1

        if result < lower_bound:
            return lower_bound
        elif result > upper_bound:
            return upper_bound
        else:
            return result


solution = Solution()
print(solution.myAtoi("42")) # output: 42
print(solution.myAtoi("   -042")) # output: -42
print(solution.myAtoi("1337c0d3")) # output: 1337
print(solution.myAtoi("0-1")) # output: 0
print(solution.myAtoi("words and 987")) # output: 0
print(solution.myAtoi("-91283472332")) # output: -2147483648
print(solution.myAtoi("3.14159")) # output: 3
print(solution.myAtoi("+-12")) # output: 0
print(solution.myAtoi("")) # output: 0
print(solution.myAtoi("+")) # output: 0
print(solution.myAtoi("-")) # output: 0
print(solution.myAtoi("   +0 123")) # output: 0
print(solution.myAtoi("-abc")) # output: 0
print(solution.myAtoi("  +  413")) # output: 0
print(solution.myAtoi("      -11919730356x")) # output: -2147483648
