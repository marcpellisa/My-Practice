def transform(legacy_data):
    response = {}
    for key, value in legacy_data.items():
        for element in value:
            response[element.lower()] = key
    return response