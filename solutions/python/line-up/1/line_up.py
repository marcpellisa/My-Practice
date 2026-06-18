def line_up(name, number):
    number=str(number)
    if number[-1]=='1' and number[-2:]!='11':
        return name + ', you are the ' + number + 'st customer we serve today. Thank you!'
    elif number[-1]=='2' and number[-2:]!='12':
        return name + ', you are the ' + number + 'nd customer we serve today. Thank you!'
    elif number[-1]=='3' and number[-2:]!='13':
        return name + ', you are the ' + number + 'rd customer we serve today. Thank you!'
    return name + ', you are the ' + number + 'th customer we serve today. Thank you!'