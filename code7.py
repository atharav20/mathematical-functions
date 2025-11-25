import time
import tracemalloc
n = int(input("Enter a number: "))
start=time.time()
tracemalloc.start()
def is_harshad(n):

    digit_sum = sum(int(d) for d in str(n))

    return n % digit_sum == 0

if is_harshad(n):
    print(n, "is a Harshad Number.")
else:
    print(n, "is NOT a Harshad Number.")
end=time.time()
peak,current=tracemalloc.get_traced_memory()
tracemalloc.stop()
print("memory utilzied is ",peak)
print("execution time is",end-start)
