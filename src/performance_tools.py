"""This module contains functions to analyze the performance of the sorting algorithms."""
import cProfile
import pstats
import timeit

from memory_profiler import profile

from algorithms import heap_sort, cocktail_shaker_sort
from src.algorithms import bubble_sort


def timeit_analysis(data):
    """Analyzes the performance of the sorting algorithms using timeit."""
    print("Timeit Analysis:")
    setup = "from algorithms import bubble_sort, heap_sort, cocktail_shaker_sort"
    for algo in ["bubble_sort", "heap_sort", "cocktail_shaker_sort"]:
        stmt = f"{algo}(data.copy())"
        time = timeit.timeit(stmt, setup=setup, globals={"data": data}, number=10)
        print(f"{algo}: {time:.5f} seconds")


def cprofile_analysis(data):
    """Analyzes the performance of the sorting algorithms using cProfile."""
    print("\ncProfile Analysis:")
    for algo in [bubble_sort, heap_sort, cocktail_shaker_sort]:
        profiler = cProfile.Profile()
        profiler.enable()
        algo(data.copy())
        profiler.disable()
        print(f"{algo.__name__}:")
        stats = pstats.Stats(profiler)
        stats.strip_dirs().sort_stats("time").print_stats(5)


@profile
def memory_analysis(data):
    """Analyzes the performance of the sorting algorithms using memory_profiler."""
    bubble_sort(data.copy())
    heap_sort(data.copy())
    cocktail_shaker_sort(data.copy())
    sorted(data.copy())
