import time
import tracemalloc
import math

n = int(input("Enter a number: "))

tracemalloc.start()
start = time.time()
def is_perfect_power(n):
    if n <= 1:
        return False
    for b in range(2, int(math.log2(n)) + 2):
        a = round(n ** (1 / b))
        if a ** b == n:
            return True
    return False
result = is_perfect_power(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Perfect Power?", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak,"bytes")
