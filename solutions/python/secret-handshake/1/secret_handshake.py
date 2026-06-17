def commands(binary_str):
    response = []
    if binary_str[-1]=='1':
        response.append('wink')
    if binary_str[-2]=='1':
        response.append('double blink')
    if binary_str[-3]=='1':
        response.append('close your eyes')
    if binary_str[-4]=='1':
        response.append('jump')
    if binary_str[-5]=='1':
        response.reverse()
    return response