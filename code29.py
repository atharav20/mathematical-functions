import time
import tracemalloc
s = int(input("Enter s: "))
n = int(input("Enter n: "))

tracemalloc.start()
start = time.time()

def polygonal_number(s, n):
    return ((s - 2) * n * (n - 1)) // 2 + n

result = polygonal_number(s, n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Polygonal Number:", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak, "bytes")
