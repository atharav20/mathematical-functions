  # 🐍 Python Number Theory and Discrete Math Library

## 🌟 Project Title
Python Number Theory and Discrete Mathematics Library for Advanced Concepts.

## 📄 Overview of the Project
This project is a dedicated Python library containing **34 modular functions** implementing complex algorithms and concepts from **Number Theory, Cryptography, and Discrete Mathematics**.The functions are designed to be complete, organized, and testable. The structure follows the "Build Your Own Project" guidelines to ensure clear documentation and implementation quality.

## ✨ Features (Functional Requirements)
The library is composed of distinct modules, each representing a specific mathematical concept or functional requirement. The core features are the 34 implemented functions:

### I. Basic Number Properties & Divisibility
* `factorial`: Calculates $n!$ for a non-negative integer $n$.
* `is_palindrome`: Checks if a number is a palindrome.
* `mean_of_digits`: Returns the average of all digits in a number.
* `digital_roots`: Repeatedly sums digits until a single digit is obtained.
*`is_abundant`: Checks if the sum of proper divisors is greater than $n$.
* `deficient`: Checks if the sum of proper divisors is less than $n$.
* `is_harshad`: Checks if a number is divisible by the sum of its digits (Harshad number).
* `isAutomorphic(N)`: Checks if a number's square ends with the number itself.
* `pronic`: Checks if a number is the product of two consecutive integers.
* `count_divisors`: Returns the number of positive divisors a number has.
* `aliquot_sum`: Returns the sum of all proper divisors of $n$.
* `amicable_numbers`: Checks if two numbers are amicable.
*`multiplicative_persistence`: Counts steps until a number's digits multiply to a single digit.
* `is_highly_composite`: Checks if a number has more divisors than any smaller number.

### II. Primality and Factorization
* `list of prime factor`: Returns the list of prime factors of a number.
* `count_distinct_prime_factors`: Returns the number of unique prime factors.
* `prime_power`: Checks if a number can be expressed as $p^k$ (p prime, $k \ge 1$).
* `mersenne_prime`: Checks if $2^p - 1$ is a prime number (given $p$ is prime).
* `twin_primes`: Generates all twin prime pairs up to a limit.
* `is_prime_miller_rabin`: Implements the probabilistic Miller-Rabin primality test with $k$ rounds,
* `pollard_rho`: Implements Pollard's $\rho$ algorithm for integer factorization.

### III. Modular Arithmetic and Advanced Math
* `mod_exp`: Efficiently calculates $(\text{base}^{\text{exponent}}) \pmod{\text{modulus}}$ (Modular Exponentiation).
* `mod_inverse`: Calculates the modular multiplicative inverse of $a \pmod m$. (Note: This function name `mod_inverse` aligns with the screenshot files).
* `order_mod`: Function to calculate the multiplicative order of an integer modulo $n$ (implied feature).
* `Chinese_Remainder_Theorem`: Solves a system of linear congruences (implied feature).
* `is_carmichael`: Checks if a composite number $n$ satisfies $a^{n-1} \equiv 1 \pmod n$ for all $a$ coprime to $n$.
* `lucas_sequence`: Generates the first $n$ Lucas numbers.
* `perfect_power`: Checks if a number can be expressed as $a^b$ where $a>0$ and $b>1$.
* `collatz_length`: Returns the number of steps for $n$ to reach 1 in the Collatz conjecture.
* `polygonal_number`: Returns the $n$-th $s$-gonal number.
* `zeta_approx`: Approximates the Riemann zeta function $\zeta(s)$ using the first 'terms' of the series.
* `partition_function`: Calculates the number of distinct ways to write $n$ as a sum of positive integers $p(n)$.

## 🛠️ Technologies/Tools Used
* **Language:** Python 3.x
* **Version Control:** Git 
* **Module Structure:** Modular and clean implementation using multiple files/modules.



## ✅ Instructions for Testing
The project adheres to the requirement for testing wherever applicable. Unit tests are crucial for verifying the mathematical correctness of these algorithms.

1.  **Install Pytest (Recommended Test Runner):**
    ```bash
    pip install pytest
    ```
2.  **Run the Tests:**
    Assuming a dedicated `tests/` directory contains all unit tests, run them from the project root:
    ```bash
    pytest
    ```

Author:-
Atharav Balaji Khonde

