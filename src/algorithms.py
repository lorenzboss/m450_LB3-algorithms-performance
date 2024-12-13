"""This module implements various sorting algorithms."""


def bubble_sort(arr):
    """Sort the list using the bubble sort algorithm."""
    length = len(arr)
    arr = arr.copy()  # Ensure immutability
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    """Sort the list using the quick sort algorithm."""
    arr = arr.copy()  # Ensure immutability
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def cocktail_shaker_sort(arr):
    """Sort the list using the cocktail shaker sort algorithm."""
    arr = arr.copy()  # Ensure immutability
    length = len(arr)
    swapped = True
    start = 0
    end = length - 1

    while swapped:
        swapped = False
        # Left to right pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        end -= 1

        # Right to left pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1

    return arr
