import time
import tracemalloc
n = int(input("Enter a number: "))
start=time.time()
tracemalloc.start()
def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors


print("Prime factors of", n, "are:", prime_factors(n))
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("memory utilzied is ",peak)
print("execution time is",end-start)
