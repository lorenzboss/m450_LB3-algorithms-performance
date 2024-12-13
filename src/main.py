"""Main file for performance tests with sorting algorithms."""

from performance_tools import timeit_analysis, cprofile_analysis, memory_analysis, pyinstrument_analysis
from utils import generate_random_list

SIZE = 1000

if __name__ == "__main__":
    print("Performance Tests with Sorting Algorithms")

    data = generate_random_list(SIZE)

    # Timeit-Analyse
    timeit_analysis(data)

    # cProfile-Analyse
    cprofile_analysis(data)

    # Memory Profiler-Analyse
    memory_analysis(data)

    # Pyinstrument-Analyse
    pyinstrument_analysis(data)
