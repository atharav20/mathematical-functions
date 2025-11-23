  **Mathematical Functions and Algorithmic Performance Analysis**

🎯 **Overview**

This project is a collection of fundamental mathematical functions implemented in Python, primarily within a Jupyter Notebook environment. Beyond simple calculation, the notebook is configured to analyze the execution time and memory usage of each function using the built-in time and tracemalloc libraries.

The goal is to provide clear, profiled implementations of common algorithms, allowing users to compare the performance characteristics (time and space complexity) of different solutions.

✨ **Features**

This notebook implements and profiles the following mathematical functions:

Factorial Calculation (factorial(n)): Computes $n!$ for a given integer $n$ using an iterative approach.

Riemann Zeta Function Approximation (zeta_function_approx(s, num_terms)): Approximates the value of the Riemann Zeta function, $\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$, by summing a specified number of terms.

Partition Function Calculation (partition_function(n)): Computes the number of ways a positive integer $n$ can be written as a sum of positive integers (i.e., $p(n)$) using a dynamic programming approach.

For each function, the notebook displays:

The calculated result.

The execution time in seconds.

The peak memory used during execution.

**Technologies & Tools Used**

Technology:-Purpose

Python 3.x              :- Core programming language.

Jupyter Notebook       :-  Environment for interactive coding and performance analysis.

time                :-     Standard library module for measuring execution time.

tracemalloc          :-    Standard library module for tracing memory allocations (used to measure memory usage).

**Steps to Install & Run the Project**

To run this project, you need a Python environment capable of running Jupyter Notebooks (e.g., Anaconda, Google Colab, or a standard Python installation with the jupyter package).

Prerequisites

Python 3.x

Jupyter Notebook (Install via pip: pip install notebook)

Running the Notebook

Download the file:
Clone the GitHub repository or download the code.ipynb file directly.

git clone [Your Repository URL Here]
cd [Your Repository Name]


Start Jupyter:
Open your terminal or command prompt in the directory where code.ipynb is located and run:

jupyter notebook


Open the notebook:
Your web browser will open to the Jupyter interface. Click on code.ipynb to open the notebook.

Execute Cells:
Run the cells sequentially by pressing Shift + Enter or clicking the "Run" button in the toolbar.

**Instructions for Testing**

The notebook is interactive and requires input in the code cells to run the functions.

Locate the function cell you wish to test (e.g., the cell containing the factorial definition and execution block).

Run the cell.

The cell will prompt you for input (e.g., Enter your number, Enter s:, Enter number of terms:).

Enter a valid integer for the input prompt and press Enter.

The results, including the final output, execution time, and memory usage, will be displayed directly below the code cell.

To test with different inputs, simply re-run the cell and provide a new value when prompted.

🖼️ Screenshots

A visual representation of the notebook output showing performance metrics:
