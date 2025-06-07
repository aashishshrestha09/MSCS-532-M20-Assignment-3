def deterministic_partition(arr: list[int], low: int, high: int) -> int:
    """
    Partition the subarray arr[low..high] around a pivot chosen as the first element.

    Elements less than the pivot are moved to its left, and greater or equal to the right.

    Args:
        arr: List of integers to partition in-place.
        low: Starting index of the subarray.
        high: Ending index of the subarray.

    Returns:
        The final index of the pivot element.
    """
    pivot = arr[low]
    i = low + 1  # index for the smaller element boundary

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Place pivot in the correct sorted position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1


def deterministic_quicksort_recursive(arr: list[int], low: int, high: int) -> None:
    """
    Recursively sort the subarray arr[low..high] using deterministic quicksort.

    Args:
        arr: List of integers to sort in-place.
        low: Starting index of the subarray.
        high: Ending index of the subarray.
    """
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort_recursive(arr, low, pi - 1)
        deterministic_quicksort_recursive(arr, pi + 1, high)


def deterministic_quicksort(arr: list[int]) -> list[int]:
    """
    Sort the entire array using deterministic quicksort.

    Args:
        arr: List of integers to sort.

    Returns:
        The sorted list (sorted in-place and returned).
    """
    if len(arr) <= 1:
        return arr
    deterministic_quicksort_recursive(arr, 0, len(arr) - 1)
    return arr
