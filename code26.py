import time
import tracemalloc
n = int(input("Enter n for Lucas Sequence: "))
tracemalloc.start()
start = time.time()
def lucas_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]
    seq = [2, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

result = lucas_sequence(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Lucas Sequence:", result)
print("Execution Time is", end - start)
print("Memory Used:", peak,"bytes")
     
