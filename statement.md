Project Definition: Algorithmic Performance Benchmarking Tool (AlgoBench)

1. Problem Statement

Researchers, students, and engineers working in scientific computing frequently implement complex mathematical algorithms (such as number theory functions, summation series, or optimization routines). A critical challenge is accurately assessing and comparing the computational efficiency—specifically, the time complexity and memory usage—of different implementations. Existing general-purpose profilers are often too complex, lack integrated visualization for comparative analysis, and require significant setup, leading to inefficient code and delayed discovery.

The core problem is the lack of a simple, specialized, web-based environment for quickly inputting, executing, and visually benchmarking mathematical algorithms against varying input sizes and constraints.

2. Scope of the Project

The project is to develop AlgoBench, a web-based utility designed to analyze the performance characteristics of user-provided mathematical algorithms.

Inclusions:

Integrated Code Editor: A clean, browser-based editor supporting Python code input.

Performance Metrics: Automatic calculation of execution time and peak memory usage for submitted algorithms.

Input Range Testing: Functionality to execute the algorithm across a user-defined range of inputs ($N$) to generate performance data.

Comparative Visualization: Interactive charts (line graphs, scatter plots) showing Time vs. $N$ and Memory vs. $N$.

Algorithm Library: A collection of pre-loaded mathematical examples (e.g., recursive vs. iterative factorial, different implementations of the partition function) for immediate testing.

Exclusions:

Support for Non-Python Languages: Initial focus is Python only.

Parallel Computing/GPU Benchmarking: Advanced benchmarking for multi-threading or hardware acceleration is out of scope.

Persistent User Accounts: Data storage will be session-based; no sign-up or permanent user profiles are included in the initial release.

3. Target Users

User Group

Primary Role

Key Needs & Pain Points

Computer Science Students

Learning algorithm analysis and data structures.

Need a visual way to confirm theoretical Big O notation (e.g., $O(N^2)$ vs. $O(N \log N)$) through practical execution.

Computational Mathematicians

Implementing and optimizing complex formulas (e.g., series approximations, numerical solvers).

Need precise memory and time profiles to choose the most efficient routine for large-scale calculations.

Data Scientists / ML Engineers

Developing custom pre-processing or feature engineering functions.

Need to quickly test custom functions for bottlenecks before deploying them in production pipelines.

4. High-Level Features

A. Code Input and Execution

Python Editor: Syntax-highlighted editor with simple execution controls.

Dynamic Input Definition: Users can define the argument variables for their algorithm and specify the range and steps for testing.

B. Automated Benchmarking

Execution Timer: Measures total wall-clock time and CPU time for the function call.

Memory Profiler: Tracks peak memory allocation used by the function during execution (similar to tracemalloc in your example).

Repeatable Testing: Automatically runs the algorithm multiple times for the same input and calculates an average to minimize external noise.

C. Visualization and Comparison

Performance Charts: Generates side-by-side or overlaid charts for:

Time (ms) vs. Input Size ($N$).

Memory (MB) vs. Input Size ($N$).

Big O Overlay: Ability to overlay theoretical complexity curves (e.g., $N^2$, $N \log N$) onto the actual measured performance data for comparison.
