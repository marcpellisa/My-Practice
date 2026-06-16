def steps(number):
    steps_taken = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number > 1:
        if number % 2 == 0:
            number = number/2
            steps_taken += 1
        else:
            number = 3*number + 1
            steps_taken += 1
    return steps_taken