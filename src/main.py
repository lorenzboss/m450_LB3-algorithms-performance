"""Main file for performance tests with sorting algorithms."""

from performance_tools import timeit_analysis, cprofile_analysis, memory_analysis, pyinstrument_analysis
from utils import generate_random_list

if __name__ == "__main__":
    print("Performance Tests with Sorting Algorithms")

    hundred_records = generate_random_list(100)
    thousand_records = generate_random_list(1000)
    ten_thousand_records = generate_random_list(10000)

    # Timeit-Analyse
    # timeit_analysis(hundred_records)
    # timeit_analysis(thousand_records)
    timeit_analysis(ten_thousand_records)

    # cProfile-Analyse
    cprofile_analysis(ten_thousand_records)

    # Memory Profiler-Analyse
    memory_analysis(ten_thousand_records)

    # Pyinstrument-Analyse
    pyinstrument_analysis(thousand_records)
    # pyinstrument_analysis(hundred_records)
    # pyinstrument_analysis(ten_thousand_records)
