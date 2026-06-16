def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in sentence:
            return False
    return True