'''
Create a function that takes a string's characters as ASCII and returns each character's 
hexadecimal value as a string

convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
'''
def convert_to_hex(txt):
    converted_list = []

#loop through the string, use ord() to convert to numbers, then use hex() on the numbers
#loop through the new list and use .lower().
#then display those values

    for i in txt:
        ord(i)
        print(i) 

    #convert then append to list?


convert_to_hex("hello world")