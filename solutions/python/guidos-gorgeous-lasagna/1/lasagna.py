EXPECTED_BAKE_TIME = 40
def bake_time_remaining(num):
    "Calculate baking time"
    solution = EXPECTED_BAKE_TIME - num
    return solution

def preparation_time_in_minutes(layers):
    "Calculate prep time"
    return layers*2

def elapsed_time_in_minutes(layers,num):
    "Calculate elapsed time"
    return num + layers*2