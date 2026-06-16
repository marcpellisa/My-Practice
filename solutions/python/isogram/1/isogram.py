def is_isogram(string):
    string = string.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    clean_string = ''
    for letter in string:
        if letter in alphabet:
            clean_string += letter
    return len(clean_string) == len(set(clean_string))