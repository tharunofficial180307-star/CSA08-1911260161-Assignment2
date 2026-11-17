"""Q6: Counting Ways to Climb Temple Steps – Naive Recursion, Memoisation, and Loop."""
from functools import lru_cache
import sys

calls = 0

def ways_naive(n):
    """Ways to climb n temple steps taking 1 or 2 steps at a time."""
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    # TODO 1 Completed
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

def ways_iterative(n):
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1

if __name__ == "__main__":
    calls = 0; print("naive:", ways_naive(25), "calls =", calls)
    calls = 0; print("memo :", ways_memo(25), "calls =", calls)
    print("System recursion limit:", sys.getrecursionlimit())
    try:
        ways_memo.cache_clear()
        ways_memo(1000)
    except RecursionError as exc:
        print("Caught RecursionError at n=1000:", type(exc).__name__)
    print("Iterative n=1000 digits:", len(str(ways_iterative(1000))))
