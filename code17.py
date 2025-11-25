import time
import tracemalloc
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
start=time.time()
tracemalloc.start()
def aliquot_sum(n):
    return sum(i for i in range(1, n) if n % i == 0)

def are_amicable(a, b):
    return aliquot_sum(a) == b and aliquot_sum(b) == a

if are_amicable(a, b):
    print(a, "and", b, "are amicable numbers.")
else:
    print(a, "and", b, "are not amicable numbers.")
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("execution time is ",end-start)
print( "memory used is",peak)
