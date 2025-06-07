import sys
import time
import csv
import os
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict, Callable
from generators import (
    generate_random_array,
    generate_sorted_array,
    generate_reverse_sorted_array,
    generate_repeated_array,
)
from deterministic_quicksort import deterministic_quicksort
from randomized_quicksort import quicksort as randomized_quicksort

# Increase recursion limit for large recursive calls
sys.setrecursionlimit(20000)

# Constants for output files and directory
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
CSV_FILENAME = "benchmark_results.csv"
PLOT_FILENAME = "benchmark_plot.png"

# Default benchmark configuration
DEFAULT_ARRAY_SIZES = [1000, 5000, 10000]
DEFAULT_TEST_TYPES = {
    "Random": generate_random_array,
    "Sorted": generate_sorted_array,
    "Reverse Sorted": generate_reverse_sorted_array,
    "Repeated": generate_repeated_array,
}


def create_output_dir(directory: str) -> None:
    """Create the output directory if it doesn't exist."""
    os.makedirs(directory, exist_ok=True)


def save_results_to_csv(
    rows: List[List], directory: str = OUTPUT_DIR, filename: str = CSV_FILENAME
) -> None:
    """
    Save benchmark results to a CSV file.

    Args:
        rows: List of rows to write, each row is a list of values.
        directory: Directory where CSV will be saved.
        filename: Name of the CSV file.
    """
    create_output_dir(directory)
    path = os.path.join(directory, filename)
    try:
        with open(path, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ["ArraySize", "TestType", "DeterministicTime", "RandomizedTime"]
            )
            writer.writerows(rows)
        print(f"Benchmark results saved to {path}")
    except IOError as e:
        print(f"Error saving CSV file: {e}")


def benchmark_sorting_algorithms(
    array_sizes: List[int] = DEFAULT_ARRAY_SIZES,
    test_types: Dict[str, Callable[[int], List[int]]] = DEFAULT_TEST_TYPES,
) -> Tuple[List[int], Dict[str, Dict[str, List[float]]]]:
    """
    Run benchmark tests for deterministic and randomized quicksort.

    Args:
        array_sizes: List of sizes of arrays to test.
        test_types: Dictionary mapping test type names to array generator functions.

    Returns:
        sizes: List of tested array sizes.
        results: Dictionary of runtimes indexed by test type and algorithm.
    """
    results = {
        test_name: {"deterministic": [], "randomized": []} for test_name in test_types
    }
    csv_rows = []

    for size in array_sizes:
        print(f"\nArray size: {size}")
        for test_name, generator in test_types.items():
            arr = generator(size)

            det_arr = arr.copy()
            start = time.perf_counter()
            deterministic_quicksort(det_arr)
            det_time = time.perf_counter() - start

            rand_arr = arr.copy()
            start = time.perf_counter()
            randomized_quicksort(rand_arr)
            rand_time = time.perf_counter() - start

            print(f"{test_name} array:")
            print(f"  Deterministic Quicksort time: {det_time:.6f} seconds")
            print(f"  Randomized Quicksort time:   {rand_time:.6f} seconds\n")

            results[test_name]["deterministic"].append(det_time)
            results[test_name]["randomized"].append(rand_time)

            csv_rows.append([size, test_name, det_time, rand_time])

    save_results_to_csv(csv_rows)
    return array_sizes, results


def plot_results(
    sizes: List[int],
    results: Dict[str, Dict[str, List[float]]],
    directory: str = OUTPUT_DIR,
    filename: str = PLOT_FILENAME,
) -> None:
    """
    Plot benchmark results and save the figure.

    Args:
        sizes: List of array sizes.
        results: Nested dict of runtimes by test type and algorithm.
        directory: Directory where plot image will be saved.
        filename: Name of the plot image file.
    """
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    axs = axs.flatten()

    for idx, (test_name, data) in enumerate(results.items()):
        ax = axs[idx]
        ax.plot(
            sizes, data["deterministic"], marker="o", label="Deterministic Quicksort"
        )
        ax.plot(
            sizes,
            data["randomized"],
            marker="x",
            linestyle="--",
            label="Randomized Quicksort",
        )

        ax.set_title(f"{test_name} Array")
        ax.set_xlabel("Array Size")
        ax.set_ylabel("Time (seconds)")
        ax.grid(True)
        ax.legend()

    plt.suptitle(
        "Deterministic vs Randomized Quicksort Performance by Input Type", fontsize=16
    )
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    create_output_dir(directory)
    plot_path = os.path.join(directory, filename)
    try:
        plt.savefig(plot_path)
        print(f"Plot saved to {plot_path}")
    except IOError as e:
        print(f"Error saving plot image: {e}")

    plt.show()


if __name__ == "__main__":
    sizes, results = benchmark_sorting_algorithms()
    plot_results(sizes, results)
