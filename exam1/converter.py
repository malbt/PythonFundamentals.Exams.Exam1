def meters_to_feet(meters: float) -> float:
    """
    This function takes a float representing a measurement in meters
    and returns the corresponding value converted to feet.
    The result is rounded to 2 decimal places.

    :param meters: A float representing a measurement in meters.
    :return: A float representing the input measurement converted to feet.
    """
    meters = float(meters)
    feet = float(float(meters) * 3.28084)
    return round(feet, 2)


def feet_to_meters(feet: float) -> float:
    """
    This function takes a float representing a measurement in feet
    and returns the corresponding value converted to meters.
    The result is rounded to 2 decimal places.

    :param feet: A float representing a measurement in feet.
    :return: A float representing the input measurement converted to meters.
    """
    feet = float(feet)
    meter = float(float(feet) * 0.3048)
    return round(meter, 2)


def kilometer_to_miles(kilometers: float) -> float:
    """
    This function takes a float representing a measurement in kilometers
    and returns the corresponding value converted to miles.
    The result is rounded to 2 decimal places.

    :param kilometers: A float representing a measurement in kilometers.
    :return: A float representing the input measurement converted to miles.
    """
    kilometers = float(kilometers)
    miles = float(float(kilometers) * 0.621371)
    return round(miles, 2)


def miles_to_kilometers(miles: float) -> float:
    """
    This function takes a float representing a measurement in miles
    and returns the corresponding value converted to kilometers.
    The result is rounded to 2 decimal places.

    :param miles: A float representing a measurement in miles.
    :return: A float representing the input measurement converted to kilometers.
    """
    mile = float(miles)
    kilometers = float(float(mile) * 1.60934)
    return round(kilometers, 2)
