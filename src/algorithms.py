
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


def heapify(arr, n, i):
    """Ensures the subtree rooted at index `i` is a max heap."""
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree


def heap_sort(arr):
    """Sorts the given list using heap sort algorithm."""
    arr = arr.copy()  # Kopiere die Eingabedaten, um sie nicht zu verändern
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr


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
