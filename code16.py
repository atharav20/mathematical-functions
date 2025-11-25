import time
import tracemalloc
n=int(input("enter a number"))
start=time.time()
tracemalloc.start()
def aliquot_sum(n):
    sum_div = sum(i for i in range(1, n) if n % i == 0)
    return sum_div
print("Sum of proper divisors:", aliquot_sum(n))
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("memory utilzied is ",current)
print("execution time is",end-start)
     
