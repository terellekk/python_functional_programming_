'''Create a function that takes a list and string.
The function should remove the letters in the string
 from the list, and return the list.'''

def remove_letters(letters, word):
    for i in word:
        if i in letters:
            letters.pop(letters.index(i))
    return letters


remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string")