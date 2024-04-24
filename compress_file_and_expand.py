# Given a file is 2,749 bytes if you create a compressed file and its 2,748 bites, thats a win its a bit smaller,
# the challenge is to get the file as small as possible, but still expand back to original.

import json
import os

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

# The filename that will be passed to this function
# is ASCII_art.txt
def encodeFile(filename, newFilename):
    with open(filename, 'r') as file:
        data = file.read()
    encodedData = encodeString(data)
    with open(newFilename, 'w') as file:
        json.dump(encodedData, file)

def decodeFile(filename):
    with open(filename, 'r') as file:
        encodedData = json.load(file)
    return decodeString(encodedData)


original_filesize = os.path.getsize("ASCII_art.txt")
print(f'Original file size: {original_filesize}')
encodeFile('ASCII_art.txt', 'ASCII_art_encoded.txt')

new_filesize = os.path.getsize("ASCII_art_encoded.txt")
print(f'New file size: {new_filesize}')
decoded = decodeFile('ASCII_art_encoded.txt')
print(decoded)