import time
import tracemalloc
p = int(input("Enter a number p: "))
start=time.time()
tracemalloc.start()
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    m = 2**p - 1
    return is_prime(m)

print("Is Mersenne prime?", is_mersenne_prime(p))
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("memory utilzied is ",peak)
print("execution time is",end-start)
