from os import remove
from typing import List, Tuple, Set, TypeVar

N = TypeVar('N', int, float)
C = TypeVar('C', List, Tuple)


def find_lowest_value(list_in: List[N]) -> N:
    """
    Returns the lowest value in a list of numbers.

    :param list_in: A list of numbers (integers and/or floats)
    :return: The lowest number in the list
    """
    lowest_val = min(list_in)
    return lowest_val


def find_highest_value(list_in: List[N]) -> N:
    """
    Returns the highest value in a list of numbers.

    :param list_in: A list of numbers (integers and/or floats)
    :return: The highest number in the list
    """
    highest_val = max(list_in)
    return highest_val


def find_value(value_to_find, values: C) -> int:
    """
    This function evaluates whether a value exists within a List or a Set.
    If the value exists, the function returns the index of the value in the collection.
    If the value does not exist, the function returns -1.

    :param value_to_find: A value that may or may not exist within a collection.
    :param values: A List or a Set.
    :return: an integer. Either the index where the value exists or -1
    """
    if value_to_find in values:
        return values.index(value_to_find)
    else:
        return -1


def compare_two_numbers(a: N, b: N) -> int:
    """
    Compares two numbers.

    If the numbers are the same, this function will return the number 0.
    If the first number is greater than the second, this function will return the number 1.
    If the second number is greater than the second, this function will return the number -1.

    :param a: The first number.
    :param b: The second number.
    :return: an integer 0, 1, or -1
    """
    if a == b:
        c = 0
        return c
    elif a > b:
        c = 1
        return c
    elif a < b:
        c = -1
        return c


def compare_two_strings(a: str, b: str) -> int:
    """
    Compares two strings.

    If the strings have the same length, this function will return the number 0.
    If the first string is longer than the second string, this function will return the number 1.
    If the second string is longer than the first string, this function will return the number -1.

    :param a: The first string.
    :param b: The second string.
    :return: an integer 0, 1, or -1
    """
    if len(a) == len(b):
        return 0
    elif len(a) > len(b):
        return 1
    elif len(b) > len(a):
        return -1


def find_common(tuple_a: Tuple, tuple_b: Tuple) -> Set:
    """
    Given two tuples, this function returns a set containing items common in both tuples.

    :param tuple_a: The first tuple.
    :param tuple_b: The second tuple.
    :return: A set containing items common on both tuples.
    """
    common_item = set(tuple_a).intersection(set(tuple_b))
    return common_item


def find_duplicates(tuple_in: Tuple) -> List:
    """
    Given a tuple, this function returns a list of the items that contain more than one instance.

    :param tuple_in: A tuple
    :return: a A list containing duplicate items in the tuple_in parameter
    """
    tuple_one = []
    duplicate = []
    tuple_one = []
    for value in tuple_in:
        if value not in tuple_one:
            tuple_one.append(value)
        elif value not in duplicate:
            duplicate.append(value)
    return sorted(duplicate)



