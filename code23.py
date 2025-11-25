import time
import tracemalloc
tracemalloc.start()
start = time.time()
def is_quadratic_residue(a, p):
    a=int(a)
    p=int(p)
    for x in range(0,p):
        if (x**2)%p==a:
            print(x)
            break
    else:
        print("no x")
is_quadratic_residue(2,5)
end = time.time()
current,peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(peak,"bytes")
print("execution time is",end - start)
