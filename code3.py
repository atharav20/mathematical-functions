import tracemalloc
import time
start = time.time()
tracemalloc.start()

def mean_of_digits(n):
  n_str = str(n)
  sum_of_digits = 0
  count_of_digits = 0
  for digit in n_str:
    sum_of_digits += int(digit)
    count_of_digits += 1
  if count_of_digits == 0:
    return 0
  else:
    return sum_of_digits / count_of_digits

end = time.time()
print(end-start)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current }; Peak was {peak}")

num1 = int(input())
print(f"The mean of digits in {num1} is: {mean_of_digits(num1)}")
