import time
import tracemalloc

def zeta_approx(s, terms):
    total = 0.0
    for n in range(1, terms+1):
        total += 1 / (n ** s)
    return total

s = float(input("Enter s: "))
terms = int(input("Enter number of terms: "))

tracemalloc.start()
start = time.time()

result = zeta_approx(s, terms)

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Zeta Approx:", result)
print("Execution Time:", end - start, "seconds")
print("Memory Used:", peak)
