import tracemalloc
import time
start = time.time()
tracemalloc.start()
def digital_root(n):
  while n > 9:
    sum_of_digits = 0
    for digit in str(n):
      sum_of_digits += int(digit)
    n = sum_of_digits
  return n
end = time.time()
print(end-start)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current }; Peak was {peak}")


num1 = int(input())
print(f"The digital root of {num1} is: {digital_root(num1)}")
