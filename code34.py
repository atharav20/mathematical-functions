import time
import tracemalloc

def partition_function(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]

n = int(input("Enter n: "))

tracemalloc.start()
start = time.time()

result = partition_function(n)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Partition p(n):", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak/1024, "KB")
