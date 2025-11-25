import time
import tracemalloc
n = int(input("Enter a number: "))
start=time.time()
tracemalloc.start()
def multiplicative_persistence(n):
    steps = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps
print("Multiplicative persistence:", multiplicative_persistence(n))
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
end=time.time()
print("memory utilzied is ",peak)
print("execution time is",end-start)
     
