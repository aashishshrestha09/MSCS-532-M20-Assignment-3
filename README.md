# Assignment 3: Understanding Algorithm Efficiency and Scalability

## Overview

This assignment explores the efficiency and scalability of two fundamental algorithms:

- Randomized Quicksort — for sorting integer datasets.
- Hash Table with Chaining — using a Universal Hash Function Family for collision resolution.

We implemented, benchmarked, and analyzed the performance of both algorithms, with a focus on:

- Time complexity analysis
- Load factor effects on hash table performance
- Dynamic resizing and its impact on runtime behavior

## Installation

### Pre-requisites

- Install [`python`](https://www.python.org/downloads/).
- Install [`pip`](https://pip.pypa.io/en/stable/installation/).

## Development

### Setup

1. Clone this repository

   ```bash
    git clone https://github.com/aashishshrestha09/MSCS-532-M20-Assignment-3.git
    cd MSCS-532-M20-Assignment-3
   ```

2. Create virtual environment for this project: `python3 -m venv .venv`.
3. Activate the virtual environment: `. .venv/bin/activate`.
4. Install as editable with "dev" packages: `pip install --editable ".[dev]"`.

## Run program

### Run Hash Table with Chaining Demo

```bash
python hash_table_chaining/main.py
```

### Run Randomized Quicksort Benchmark

```bash
python randomized_quicksort/benchmark.py
```

### Run Both Hash Table and Quicksort Benchmarks Together

```bash
python run_benchmarks.py
```

## Project Structure

```
.
├── hash_table_chaining
│   ├── __init__.py
│   ├── hash_table.py
│   ├── main.py
│   └── universal_hash.py
├── pyproject.toml
├── randomized_quicksort
│   ├── __init__.py
│   ├── benchmark.py
│   ├── deterministic_quicksort.py
│   ├── generators.py
│   ├── output
│   │   ├── benchmark_plot.png
│   │   └── benchmark_results.csv
│   └── randomized_quicksort.py
├── README.md
└── run_benchmarks.py

```

### Notes

- Benchmark results and plots are saved in the randomized_quicksort/output directory.
- The hash table dynamically resizes when the load factor exceeds 0.75 to maintain efficient operation.
