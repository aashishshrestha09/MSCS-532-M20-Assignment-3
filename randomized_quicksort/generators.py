import random


def generate_random_array(size):
    """
    Generates a randomly ordered array of the specified size.

    Parameters:
        size (int): Number of elements in the array.

    Returns:
        list: Random array.
    """
    return [random.randint(1, 10000) for _ in range(size)]


def generate_sorted_array(size):
    """
    Generates an already sorted array in ascending order.

    Parameters:
        size (int): Number of elements in the array.

    Returns:
        list: Sorted array.
    """
    return list(range(1, size + 1))


def generate_reverse_sorted_array(size):
    """
    Generates a reverse-sorted array in descending order.

    Parameters:
        size (int): Number of elements in the array.

    Returns:
        list: Reverse sorted array.
    """
    return list(range(size, 0, -1))


def generate_repeated_array(size, value=42):
    """
    Generates an array where all elements have the same repeated value.

    Parameters:
        size (int): Number of elements.
        value (int, optional): Value to repeat. Defaults to 42.

    Returns:
        list: Array of repeated values.
    """
    return [value] * size
