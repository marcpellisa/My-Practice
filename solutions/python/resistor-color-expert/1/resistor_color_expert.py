def resistor_label(colors):
    color_values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    tolerances = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green": "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%",
    }

    if len(colors) == 1:
        return "0 ohms"

    digits = colors[:-2]
    multiplier = color_values[colors[-2]]
    tolerance = tolerances[colors[-1]]

    value = int("".join(str(color_values[color]) for color in digits))
    value *= 10 ** multiplier

    if value >= 1_000_000_000:
        value /= 1_000_000_000
        unit = "gigaohms"
    elif value >= 1_000_000:
        value /= 1_000_000
        unit = "megaohms"
    elif value >= 1_000:
        value /= 1_000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{value:g} {unit} {tolerance}"