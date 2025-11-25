
import random
import time
import tracemalloc

def is_prime_miller_rabin(n, k):
    if n < 2:
        return False
    small = [2,3,5,7,11,13]
    if n in small:
        return True
    if any(n % p == 0 for p in small):
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d//=2
        r+=1

    for _ in range(k):
        a = random.randrange(2, n-2)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

n = int(input("Enter number: "))
k = int(input("Enter rounds k: "))

tracemalloc.start()
start = time.time()

result = is_prime_miller_rabin(n, k)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Probably Prime?", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak)
