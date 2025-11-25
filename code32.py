import random
import math
import time
import tracemalloc

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randrange(2, n - 1)
    y = x
    c = random.randrange(1, n - 1)
    d = 1
    while d == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        d = math.gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
    return d

n = int(input("Enter number: "))

tracemalloc.start()
start = time.time()

result = pollard_rho(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Factor Found:", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak)
