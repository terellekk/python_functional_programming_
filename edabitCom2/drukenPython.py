'''Python got drunk and the built-in functions str() and int() are acting odd:
str(4) ➞ 4

str("4") ➞ 4

int("4") ➞ "4"

int(4) ➞ "4"

You need to create two functions to substitute str() and int().
A function called int_to_str() that converts integers into strings
and a function called str_to_int() that converts strings into integers.

int_to_str(4) ➞ "4"

str_to_int("4") ➞ 4

int_to_str(29348) ➞ "29348"'''

def int_to_str(num):
    if num == int:
        new2 = str(num)
        return new2
print(int_to_str(4))

def str_to_int(num):
    if num == str:
        new = int(num)
        return new
print(int_to_str("4"))