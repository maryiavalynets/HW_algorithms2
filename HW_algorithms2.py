# 1. Split in Half
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

st = "bbbbbcaaaaa"

def split_in_half(st):

    if len(st) % 2 == 0:
        part_one = st[0:len(st) // 2]
        part_two = st[(len(st) // 2):]
    else:
        part_one = st[0:((len(st) // 2)+1)]
        part_two = st[((len(st)//2)+1):]

    return part_two + part_one


print(split_in_half(st))

 #2. Unique Characters in String
#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.

string = "abcde"

def unique_charecters(string):

    string = string.lower()
    d = ""

    for letter in string:
        if letter not in d:
            d += letter

    if d == string:
        return True
    else:
        return False

print(unique_charecters(string))