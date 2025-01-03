# Algorithms Performance Testing

This project is designed to analyze and compare the performance and memory usage of several popular
sorting algorithms using Python. It includes the following sorting algorithms:

- Bubble Sort
- Quick Sort
- Cocktail Shaker Sort

## Features

- **Performance Testing**: Compare the execution time of different sorting algorithms on a list of
  random numbers.
- **Memory Analysis**: Track memory usage during the execution of sorting algorithms.
- **Algorithm Implementations**: Detailed implementations of Bubble Sort, Cocktail Shaker Sort, and Quick
  Sort.

## Requirements

To run the performance tests and memory analysis, you need to have the following Python packages
installed:

You can install the required packages using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the repository** to your local machine.

2. **Run the Performance Tests**

   To execute the performance tests and analyze sorting algorithms, simply run the script:

   ```bash
   python src/main.py
   ```

   This will print out the performance results for each algorithm, including the execution time for
   sorting a list of
   random numbers.

   **Warning**: The performance tests may take A FEW MINUTES to complete, depending on the size of
   the input list and the number of iterations.

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

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent
elements, and swaps them if they are in the wrong order. This process continues until the list is
sorted.

### 2. **Merge Sort**

Merge Sort is an efficient, stable, and divide-and-conquer sorting algorithm. It divides the
unsorted list into n sublists, each containing one element, and then merges those sublists to
produce a sorted list.

### 3. **Quick Sort**

Quick Sort is a divide-and-conquer algorithm. It selects a pivot element from the array and
partitions the other elements into two sub-arrays, according to whether they are less than or
greater than the pivot. The sub-arrays are recursively sorted.

## Notes

- The algorithms have been selected to demonstrate a wide range of performance, from inefficient (
  Bubble Sort) to highly efficient (Quick Sort).
- The goal of this project is to provide performance insights and a comparative analysis of sorting
  algorithms, especially in terms of time and memory usage.