import time
import tracemalloc
n = int(input("Enter a number: "))
start=time.time()
tracemalloc.start()
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_prime_power(n):
    for p in range(2, int(n**0.5) + 1):
        if is_prime(p):
            k = 1
            while p**k <= n:
                if p**k == n:
                    return True
                k += 1
    return False

print("Is prime power?", is_prime_power(n))
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("memory utilzied is ",peak)
print("execution time is",end-start)
