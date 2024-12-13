
"""This module contains implementations of various sorting algorithms."""


def bubble_sort(arr):
    """Sorts the given list using bubble sort algorithm."""
    length = len(arr)
    arr = arr.copy()  # Kopiere die Eingabedaten, um sie nicht zu verändern
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def cocktail_shaker_sort(arr):
    """Sorts the given list using cocktail shaker sort algorithm."""
    arr = arr.copy()  # Kopiere die Eingabedaten, um sie nicht zu verändern
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Von links nach rechts
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Wenn keine Elemente mehr vertauscht wurden, ist die Liste sortiert
        if not swapped:
            break

        # Anpassen des Endpunkts
        end -= 1
        swapped = False

        # Von rechts nach links
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Anpassen des Startpunkts
        start += 1

    return arr
