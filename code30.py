import time
import tracemalloc
n = int(input("Enter number: "))

tracemalloc.start()
start = time.time()

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def is_carmichael(n):
    if n < 2 or is_prime(n):
        return False
    temp = n
    for p in range(2, int(n**0.5) + 1):
        if temp % p == 0:
            if (temp // p) % p == 0:
                return False
            if (n - 1) % (p - 1) != 0:
                return False
    return True

result = is_carmichael(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Carmichael?", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak, "bytes")
