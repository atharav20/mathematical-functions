import tracemalloc
import time
start = time.time()
tracemalloc.start()
def factorial(n):
    factorial = 1
    for x in range(1,n+1):
        factorial*= x
    print(factorial)
end = time.time()
print(end-start)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current }; Peak was {peak}")

n = int(input("enter your number"))
factorial(n)
