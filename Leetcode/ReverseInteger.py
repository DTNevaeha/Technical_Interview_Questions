"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""


def reverse(number: int) -> int:
	if number == 0:
		return 0
	
	test_number = 0
	number_string = str(number)
	
	test_number = number_string[::-1]
	if test_number.endswith("-"):
		test_number = test_number.rstrip("-")
		newNumber = "-" + test_number
	else: newNumber = test_number

	lower_bound = -2**31
	upper_bound = 2**31 - 1

	if int(newNumber) < lower_bound or int(newNumber) > upper_bound:
		return 0
	else:
		return int(newNumber)


print(reverse(123))  # 321
print(reverse(-123))  # -321
print(reverse(0))  # 0
print(reverse(120))  # 21
print(reverse(1534236469))  # 0
