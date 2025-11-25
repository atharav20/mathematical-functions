import time
import tracemalloc
n = int(input("Enter a number: "))
start=time.time()
tracemalloc.start()
def is_automorphic(n):
    square = n ** 2
    # Check if square ends with the number itself
    return str(square).endswith(str(n))

if is_automorphic(n):
    print(n, "is an Automorphic Number.")
else:
    print(n, "is NOT an Automorphic Number.")
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("memory utilzied is ",peak)
print("execution time is",end-start)
