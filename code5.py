import tracemalloc
import time

start = time.time()
tracemalloc.start()

def is_abundant(n):
  proper_divisors_sum = 0
  for i in range(1, n // 2 + 1):
    if n % i == 0:
      proper_divisors_sum += i
  return proper_divisors_sum > n

end = time.time()
print(end-start)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current }; Peak was {peak}")

num1 =int(input())
if is_abundant(num1):
  print(f"{num1} is an abundant number")
else:
  print(f"{num1} is not an abundant number")
