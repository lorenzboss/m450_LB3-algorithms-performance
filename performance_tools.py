import timeit
import cProfile
import pstats
from memory_profiler import profile
from algorithms import bubble_sort, merge_sort, quick_sort


def timeit_analysis(data):
    print("Timeit Analysis:")
    setup = "from algorithms import bubble_sort, merge_sort, quick_sort"
    for algo in ["bubble_sort", "merge_sort", "quick_sort"]:
        stmt = f"{algo}(data.copy())"
        time = timeit.timeit(stmt, setup=setup, globals={"data": data}, number=10)
        print(f"{algo}: {time:.5f} seconds")


def cprofile_analysis(data):
    print("\ncProfile Analysis:")
    for algo in [bubble_sort, merge_sort, quick_sort]:
        profiler = cProfile.Profile()
        profiler.enable()
        algo(data.copy())
        profiler.disable()
        print(f"{algo.__name__}:")
        stats = pstats.Stats(profiler)
        stats.strip_dirs().sort_stats("time").print_stats(5)


@profile
def memory_analysis(data):
    bubble_sort(data.copy())
    merge_sort(data.copy())
    quick_sort(data.copy())
    sorted(data.copy())