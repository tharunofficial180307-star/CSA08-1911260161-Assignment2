"""Q7: Day-4 Design Challenge – Iterative DP Redesign for Temple Step Counter."""
import time
import sys

def ways_iterative_dp(n):
    if n < 0:
        raise ValueError("Steps cannot be negative")
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    for n in (25, 1000, 10000):
        t0 = time.perf_counter()
        ans = ways_iterative_dp(n)
        dt = (time.perf_counter() - t0) * 1000
        print(f"n={n:5d} | Result digits: {len(str(ans)):4d} | Time: {dt:.4f} ms | State mem: {sys.getsizeof(ans)} bytes")
