import time
import tracemalloc
limit = int(input("Enter limit: "))
start=time.time()
tracemalloc.start()
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def twin_primes(limit):
    for i in range(2, limit - 1):
        if is_prime(i) and is_prime(i + 2):
            print(f"({i}, {i + 2})")

print("Twin prime pairs up to", limit, ":")
twin_primes(limit)
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("memory utilzied is ",peak)
print("execution time is",end-start)
