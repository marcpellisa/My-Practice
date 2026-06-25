def sum_of_multiples(limit, multiples):
    result = set()
    for number in multiples:
        if number == 0:
            continue

        multipl = (limit - 1) // number
        if multipl > 0:
            for i in range(1, multipl + 1):
                result.add(i * number)

    return sum(result)