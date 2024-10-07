def optimized_bubble_sort(arr: list[int]) -> list[int]:
    """
    Perform optimized bubble sort on a list of integers.

    Args:
        arr (list): List of integers to sort.

    Returns:
        list: Sorted list of integers.

    Example:
        >>> optimized_bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
