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

You can install the required packages using `pip`:

```bash
pip install -r requirements.txt
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

## Test and Lint the Code

To run tests and lint the code, use the following commands:

```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
pylint src tests
pytest --cov=algorithms --cov-report=term
```

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

## Notes

- The algorithms have been selected to demonstrate a wide range of performance, from inefficient (Bubble Sort) to highly
  efficient (Merge Sort and Quick Sort).
- The goal of this project is to provide performance insights and a comparative analysis of sorting algorithms,
  especially in terms of time and memory usage.