from typing import Callable, List
import random


def generate_list(start: int, stop: int, step: int = 1) -> List[int]:
    """
    Generate a list of integers.

    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param step: How many digits apart each number is from the others around it.
    :return: A list of integers.
    """
    my_list = []
    i = start
    while i < stop:
        my_list.append(i)
        i = i + step
    return my_list


def generate_list_with_strategy(start: int, stop: int, step: int, strategy: Callable) -> List[int]:
    """
    Generate a list of integers.

    :param start: Where to start the list (inclusive).
    :param stop: Where to stop the list (exclusive).
    :param step: How many digits apart each number is from the others around it.
    :param strategy: A function to manipulate each digit .
    :return: A list of integers.
    """
    pass  # implement me
