import time
import tracemalloc
tracemalloc.start()
start = time.time()
def crt(remainders, moduli):
    r=int(remainders)
    m=int(moduli)
    x=0
    for x in range(0,m):
        if (x % m)==r:
            print(r)
    x=x+1
crt(2,7)
end = time.time()
current,peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(peak,"bytes")
print("execution time is",end - start)
     
