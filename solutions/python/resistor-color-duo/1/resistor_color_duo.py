def value(colors):
    color_list = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    final_value = ''
    if colors=='':
        return ''
    for i in range(len(colors)):
        if i<2:
            final_value += str(color_list.index(colors[i]))
    return int(final_value)