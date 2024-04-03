# How to reverse a string
# This is string complexity 0(n)
# because a new string of length n is created to store the reversed string.
string1 = "Please make me reversed!"
string2 = string1[::-1]
print(string2)

# This wont work because you're starting at the beginning of the sequence and trying to step backwards, this slice will
#  not return any elements. It's trying to go backwards from the start, which isn't possible.
string3 = string1[0:5:-1]
print(string3)

# Start atfter the given index to the end
string4 = string1[:6:-1]
print(string4)

# Start at the beginning and go to the given index
string5 = string1[:5][::-1]
print(string5)