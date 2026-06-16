def label(colors):
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    first = color_list.index(colors[0])
    second = color_list.index(colors[1])
    multiplier = color_list.index(colors[2])

    value = int(str(first) + str(second)) * (10 ** multiplier)

    if value >= 1_000_000_000:
        return str(value // 1_000_000_000) + " gigaohms"
    elif value >= 1_000_000:
        return str(value // 1_000_000) + " megaohms"
    elif value >= 1_000:
        return str(value // 1_000) + " kiloohms"
    else:
        return str(value) + " ohms"