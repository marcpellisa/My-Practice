"Armstrong number verifyer"

def is_armstrong_number(number):
    "Transforming number int into str in order to separate it"
    number_string = str(number)
    total_amount = 0
    for i, numbers in enumerate(number_string):
        "Adding up every independent number squared"
        total_amount += int(numbers)**len(number_string)
    return total_amount == number
