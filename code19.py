import time
import tracemalloc
n = int(input("Enter a number: "))
start=time.time()
tracemalloc.start()
def num_divisors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)

def is_highly_composite(n):
    n_div = num_divisors(n)
    for i in range(1, n):
        if num_divisors(i) >= n_div:
            return False
    return True

if is_highly_composite(n):
    print(n, "is a highly composite number.")
else:
    print(n, "is not a highly composite number.")
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
end=time.time()
print("memory utilzied is ",peak)
print("execution time is",end-start)
