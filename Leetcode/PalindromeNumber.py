'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''


def isPalindrome(x) -> bool:
    """
    :type x: int
    :rtype: bool
    """
    reversed = str(x)[::-1]
    if reversed.endswith("-"):
        return False
    if str(x) == reversed:
        return True
    else: return False

print(isPalindrome(121)) # output: true
print(isPalindrome(-121)) # output: false
print(isPalindrome(10)) # output: false