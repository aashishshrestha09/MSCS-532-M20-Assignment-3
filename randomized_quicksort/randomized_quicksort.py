import random
from generators import (
    generate_random_array,
    generate_sorted_array,
    generate_reverse_sorted_array,
    generate_repeated_array,
)


def randomized_partition(arr, low, high):
    """
    Partitions the subarray arr[low..high] using a randomly selected pivot element.

    Steps:
    1. Randomly select a pivot index between low and high inclusive.
    2. Swap the pivot element with the element at 'high' to use the standard partition scheme.
    3. Rearrange elements so that those less than or equal to the pivot come before it,
       and those greater come after.
    4. Return the final position of the pivot.

    This randomization ensures that the pivot choice is unbiased, improving
    average-case performance and avoiding worst-case behavior on already sorted arrays.

    Parameters:
    - arr: list[int], the array to partition
    - low: int, starting index of the subarray
    - high: int, ending index of the subarray

    Returns:
    - int: index position of the pivot after partitioning
    """
    pivot_index = random.randint(low, high)
    # Swap chosen pivot with last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]

    i = low - 1  # place for the smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low, high):
    """
    Recursively applies Randomized Quicksort on the subarray arr[low..high].

    The algorithm partitions the array around a randomly chosen pivot element,
    then recursively sorts the left and right subarrays.

    Parameters:
    - arr: list[int], array to be sorted
    - low: int, starting index
    - high: int, ending index
    """
    if low < high:
        # Partition the array and get the pivot index
        pi = randomized_partition(arr, low, high)
        # Recursively sort elements before pivot
        randomized_quicksort(arr, low, pi - 1)
        # Recursively sort elements after pivot
        randomized_quicksort(arr, pi + 1, high)


def quicksort(arr):
    """
    Public function to perform Randomized Quicksort on an entire array.

    Handles edge cases:
    - Empty arrays: returns immediately without sorting
    - Single-element arrays: returns immediately (already sorted)

    Parameters:
    - arr: list[int], array to sort

    Returns:
    - list[int]: sorted array (in-place modification)
    """
    if arr is None or len(arr) <= 1:
        # Trivially sorted
        return arr
    randomized_quicksort(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    # Small test cases
    test_cases = {
        "Empty array": [],
        "Single element": [42],
        "All repeated": [7, 7, 7, 7, 7],
        "Already sorted": list(range(10)),
        "Reverse sorted": list(range(10, 0, -1)),
        "Random with duplicates": [3, 1, 4, 1, 5, 9, 2, 6, 5],
    }

    for name, arr in test_cases.items():
        print(f"{name}:")
        original = arr.copy()
        sorted_arr = quicksort(arr.copy())
        print(f"  Original: {original}")
        print(f"  Sorted:   {sorted_arr}\n")

    # Benchmarking large arrays
    sizes = [10, 20]

    for size in sizes:
        print(f"\nArray Size: {size}")

        arrays = {
            "Random": generate_random_array(size),
            "Sorted": generate_sorted_array(size),
            "Reverse Sorted": generate_reverse_sorted_array(size),
            "Repeated": generate_repeated_array(size),
        }

        for name, arr in arrays.items():
            print(f"{name}:")
            original = arr.copy()
            sorted_arr = quicksort(arr.copy())
            print(f"  Original: {original}")
            print(f"  Sorted:   {sorted_arr}\n")
