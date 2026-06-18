def square_of_sum(number):
    count = 0
    for i in range(0,number):
        count += i+1
    return count**2


def sum_of_squares(number):
    count = 0
    for i in range(0,number):
        count += (i+1)**2
    return count


def difference_of_squares(number):
    return square_of_sum(number)-sum_of_squares(number)
