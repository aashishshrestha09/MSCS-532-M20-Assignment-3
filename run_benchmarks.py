import subprocess


def run_all_benchmarks():
    """
    Runs both the Quicksort benchmark suite and
    the Hash Table Chaining test program sequentially.
    """
    print("Running Quicksort Benchmarks...")
    subprocess.run(["python", "randomized_quicksort/benchmark.py"], check=True)

    print("\nRunning Hash Table Chaining Tests...")
    subprocess.run(["python", "hash_table_chaining/main.py"], check=True)


if __name__ == "__main__":
    run_all_benchmarks()
