def is_armstrong_number(number):
    number_string = str(number)
    res = 0
    for i in range(len(number_string)):
        res += int(number_string[i])**len(number_string)
    return res == number
