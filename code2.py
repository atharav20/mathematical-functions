import tracemalloc
import time
start = time.time()
tracemalloc.start()
def is_palindrome(n):
  n_str = str(n)
  n_str_reversed = n_str[::-1]
  return n_str == n_str_reversed
end = time.time()
print(end-start)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current }; Peak was {peak}")

num = input()
if is_palindrome(num):
  print(f"{num} is a palindrome")
else:
  print(f"{num} is not a palindrome")
