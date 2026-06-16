def is_valid(isbn):
    numbers = '0123456789X'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
    new_isbn=''
    for character in isbn:
        if character in numbers:
            new_isbn += character
        elif character in alphabet:
            return False
    if len(new_isbn)<10 or len(new_isbn)>10:
        return False
    if 'X' in new_isbn and 'X' not in new_isbn[-1]:
        return False
    if new_isbn[-1]=='X':
        return (int(new_isbn[0]) * 10 + int(new_isbn[1]) * 9 + int(new_isbn[2]) * 8 + int(new_isbn[3]) * 7 + int(new_isbn[4]) * 6 + int(new_isbn[5]) * 5 + int(new_isbn[6]) * 4 + int(new_isbn[7]) * 3 + int(new_isbn[8]) * 2 + 10 * 1) % 11 == 0
    return (int(new_isbn[0]) * 10 + int(new_isbn[1]) * 9 + int(new_isbn[2]) * 8 + int(new_isbn[3]) * 7 + int(new_isbn[4]) * 6 + int(new_isbn[5]) * 5 + int(new_isbn[6]) * 4 + int(new_isbn[7]) * 3 + int(new_isbn[8]) * 2 + int(new_isbn[9]) * 1) % 11 == 0
        