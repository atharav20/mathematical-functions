import time
import tracemalloc
n = int(input("Enter number: "))

tracemalloc.start()
start = time.time()

def collatz_length(n):
    steps = 0
    while n != 1:
        n = n//2 if n%2==0 else 3*n+1
        steps += 1
    return steps

result = collatz_length(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Steps:", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak, "bytes")
