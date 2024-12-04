# Algorithms Performance Testing

This project is designed to analyze and compare the performance and memory usage of several popular sorting algorithms
using Python. It includes the following sorting algorithms:

- Bubble Sort
- Merge Sort
- Quick Sort
- Python's built-in `sorted()` function (Timsort)

## Features

- **Performance Testing**: Measure the execution time of each algorithm using Python's `timeit` module.
- **Memory Analysis**: Track memory usage and increments during sorting operations using the `memory_profiler` package.
- **Algorithms**: Includes simple implementations of Bubble Sort, Merge Sort, and Quick Sort, as well as Python’s
  built-in `sorted()` function.

## Requirements

To run the performance tests and memory analysis, you need to have the following Python packages installed:

- `memory_profiler` (for memory usage analysis)
- `timeit` (for performance testing)

You can install the required package(s) using `pip`:

```bash
pip install memory-profiler
```

## Usage

1. **Clone the repository** to your local machine.

2. **Run the Performance Tests**

   To execute the performance tests and analyze sorting algorithms, simply run the script:

   ```bash
   python main.py
   ```

   This will print out the performance results for each algorithm, including the execution time for sorting a list of
   random numbers.

3. **Run Memory Analysis**

   You can track memory usage by running the following command:

   ```bash
   python -m memory_profiler performance_tools.py
   ```

   This will display the memory usage increments during the execution of each sorting algorithm.

## Algorithm Implementations

### 1. **Bubble Sort**

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps
them if they are in the wrong order. This process continues until the list is sorted.

- Time complexity: O(n²)
- Space complexity: O(1)

### 2. **Merge Sort**

Merge Sort is an efficient, stable, and divide-and-conquer sorting algorithm. It divides the unsorted list into n
sublists, each containing one element, and then merges those sublists to produce a sorted list.

- Time complexity: O(n log n)
- Space complexity: O(n)

### 3. **Quick Sort**

Quick Sort is a divide-and-conquer algorithm. It selects a pivot element from the array and partitions the other
elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are
recursively sorted.

- Time complexity: O(n log n) on average, O(n²) in the worst case
- Space complexity: O(log n) on average

### 4. **Python's Built-in `sorted()` Function (Timsort)**

The Python `sorted()` function uses Timsort, a hybrid sorting algorithm derived from merge sort and insertion sort. It
is efficient for real-world data and guarantees stable sorting.

- Time complexity: O(n log n)
- Space complexity: O(n)
know if you'd like to make any adjustments or add more specific details!