# How to check if your string is a palindrome

def is_palindrome(teststr):
    # Remove punctuation and convert to lowercase
    teststr = ''.join(c for c in teststr if c.isalnum()).lower()
    # Compare the string with its reverse
    return teststr == teststr[::-1]

total = 0
test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.", "Race car!"]

for word in test_words:
    is_pal = is_palindrome(word)
    total += is_pal
    print(f'"{word}" is a palindrome: {is_pal}')

print(f'Total palindromes: {total}')