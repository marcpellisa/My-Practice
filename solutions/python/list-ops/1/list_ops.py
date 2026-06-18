def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for element in lists:
        result.extend(element)
    return result


def filter(function, list):
    result = []
    for element in list:
        if function(element)==True:
            result.append(element)
    return result


def length(list):
    return len(list)


def map(function, list):
    result =[]
    for element in list:
        result.append(function(element))
    return result


def foldl(function, list, initial):
    for element in list:
        initial = function(initial, element)
    return initial


def foldr(function, list, initial):
    list = list[::-1]
    for element in list:
        initial = function(initial, element)
    return initial


def reverse(list):
    return list[::-1]
