"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    locomotive = each_wagons_id[2]
    return [locomotive] + missing_wagons + each_wagons_id[3:] + each_wagons_id[:2]

    


def add_missing_stops(route,**stops):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    
    route['stops'] = []

    for stop in stops:
        route['stops'].append(stops[stop])

    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """

    for information in more_route_information:
        route[information] = more_route_information[information]

    return route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """

    sorted_wagons = []

    for i in range(len(wagons_rows[0])):
        new_row = []

        for wagon_set in wagons_rows:
            new_row.append(wagon_set[i])

        sorted_wagons.append(new_row)

    return sorted_wagons

    " return [list(row) in row for zip(*wagons_rows)]"