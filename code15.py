
import time
import tracemalloc
n=int(input("enter a number"))
start=time.time()
tracemalloc.start()
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

print("Number of divisors:", count_divisors(n))
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("memory utilzied is ",peak)
print("execution time is",end-start)
