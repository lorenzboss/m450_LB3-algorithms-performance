"""This module contains functions to analyze the performance of the sorting algorithms."""
import cProfile
import pstats
import timeit

from memory_profiler import profile
from pyinstrument import Profiler

from algorithms import quick_sort, cocktail_shaker_sort, bubble_sort


def timeit_analysis(data):
    """Analyzes the performance of the sorting algorithms using timeit."""
    print(f"\nTimeit Analysis with {len(data)} data records:")
    setup = "from algorithms import bubble_sort, cocktail_shaker_sort, quick_sort"
    header_format = "{:<25} {:>10}"
    print(header_format.format("Algorithm", "Time (s)"))
    print("-" * 35)
    for algo in ["bubble_sort", "cocktail_shaker_sort", "quick_sort"]:
        stmt = f"{algo}(data.copy())"
        time = timeit.timeit(stmt, setup=setup, globals={"data": data}, number=10)
        print(header_format.format(algo, f"{time:.5f}"))


def cprofile_analysis(data):
    """Analyzes the performance of the sorting algorithms using cProfile."""
    print(f"\ncProfile Analysis with {len(data)} data records:")
    for algo in [bubble_sort, cocktail_shaker_sort, quick_sort]:
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
    print(f"\nMemory Analysis with {len(data)} data records:")
    bubble_sort(data.copy())
    cocktail_shaker_sort(data.copy())
    quick_sort(data.copy())
    sorted(data.copy())


def pyinstrument_analysis(data):
    """Analyzes the performance of the sorting algorithms using Pyinstrument."""
    print(f"\nPyinstrument Analysis with {len(data)} data records:")
    profiler = Profiler()
    profiler.start()
    bubble_sort(data.copy())
    cocktail_shaker_sort(data.copy())
    quick_sort(data.copy())
    profiler.stop()
    print(profiler.output_text(unicode=True, color=True))
