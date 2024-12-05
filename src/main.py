"""Main file for performance tests with sorting algorithms."""

from performance_tools import timeit_analysis, cprofile_analysis, memory_analysis
from utils import generate_random_list

SIZE = 5000

if __name__ == "__main__":
    print("Performance Tests with Sorting Algorithms")

    data = generate_random_list(SIZE)

    # Timeit-Analyse
    timeit_analysis(data)

    # cProfile-Analyse
    cprofile_analysis(data)

    # Memory Profiler-Analyse (TODO: Does not work yet, Bubble sort always wins!)
    memory_analysis(data)
