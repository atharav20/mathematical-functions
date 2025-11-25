import time
import tracemalloc
tracemalloc.start()
start = time.time()
def mod_inverse(a, m):
    a = int(a)
    m = int(m)
    for x in range(1, m):
        if (a * x) % m == 1:
            print(x)
            break
    else:
        print("no inverse")
mod_inverse(2,5)
end = time.time()
current,peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(peak,"bytes")
print("execution time is",end - start)
     
