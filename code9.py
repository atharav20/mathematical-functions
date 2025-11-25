import time
import tracemalloc
n = int(input("Enter a number: "))
start=time.time()
tracemalloc.start()
def is_pronic(n):
    # A pronic number = product of two consecutive integers
    for i in range(1, n + 1):
        if i * (i + 1) == n:
            return True
    return False


if is_pronic(n):
    print(n, "is a Pronic Number.")
else:
    print(n, "is NOT a Pronic Number.")
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("memory utilzied is ",peak)
print("execution time is",end-start)
     
