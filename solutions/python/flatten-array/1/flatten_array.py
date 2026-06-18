def flatten(iterable):
    result = []
    for element in iterable:
        if isinstance(element, list):
            result.extend(flatten(element))
        elif isinstance(element, int)==False:
            continue
        else:
            result.append(element)
    return result