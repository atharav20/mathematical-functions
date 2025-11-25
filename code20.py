import time
import tracemalloc
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
modulus = int(input("Enter modulus: "))
start=time.time()
tracemalloc.start()
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

print("Result:", mod_exp(base, exponent, modulus))
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
end=time.time()
print("memory utilzied is ",peak)
print("execution time is",end-start)
     
