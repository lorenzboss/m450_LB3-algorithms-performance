"""Tests for the sorting algorithms."""
import pytest

from algorithms import bubble_sort, quick_sort, cocktail_shaker_sort


@pytest.mark.parametrize("algorithm", [bubble_sort, quick_sort, cocktail_shaker_sort])
def test_sort_correctness(algorithm):
    """Test that sorting algorithms sort the list correctly."""
    data = [5, 2, 9, 1, 5, 6]
    sorted_data = sorted(data)  # Python's built-in sorted function as reference
    result = algorithm(data)  # Algorithmus gibt die sortierte Liste zurück
    assert result == sorted_data, f"{algorithm.__name__} failed to sort correctly."
