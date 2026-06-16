def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[key:] + alphabet[:key]
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NEW_ALPHABET = ALPHABET[key:] + ALPHABET[:key]
    solution = ''
    for letter in text:
        if letter not in alphabet and letter not in ALPHABET:
            solution += letter
        for i in range(26):
            if alphabet[i] == letter:
                solution += new_alphabet[i]
            elif ALPHABET[i] == letter:
                solution += NEW_ALPHABET[i]
    return solution