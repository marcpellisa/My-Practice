def find(search_list, value):
    position = 0
    
    if value not in search_list:
        raise ValueError("value not in array")
    
    for i in range(len(search_list)):
        mid_position = len(search_list)//2
        if search_list[mid_position] == value:
            return position + mid_position
        elif search_list[mid_position] < value:
            position += mid_position + 1
            search_list = search_list[mid_position+1:]
        elif search_list[mid_position] > value:
            search_list = search_list[:mid_position]
        