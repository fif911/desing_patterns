"""
for multiprocessing in case of CPU bound task
https://www.youtube.com/watch?v=4EBs1BDvuzk&t=386s
"""

import time
import tracemalloc

# We'll determine the factorial for these numbers

NUMBERS = 50000, 50001, 50002, 50003, 50004, 50005, 50006, 50007  # to demonstrate the performance boots


# NUMBERS = 500, 501, 502, 503, 504, 505, 506, 507  # to demonstrate overhead problem


def factorial(n):
    """Great for multiprocessing, because it:

    - Takes a while (for large numbers)!
    - Is referentially transparent

    factorial(3) == 3 × 2 × 1 == 6
    """

    print('start: factorial({})'.format(n))
    f = 1
    for i in range(1, n + 1):
        f *= i
    print('done:  factorial({})'.format(n))
    return f


if __name__ == '__main__':
    # With a for loop in a single process
    t0 = time.time()
    result = []
    for n in NUMBERS:
        result.append(factorial(n))
    t1 = time.time()
    print('Execution took {:.4f}'.format(t1 - t0))

    # With map() in a single process
    t0 = time.time()
    result = list(map(factorial, NUMBERS))
    t1 = time.time()
    print('Execution took {:.4f}'.format(t1 - t0))

    # With multiprocessing.Pool()
    tracemalloc.start()
    start_time = time.time()
    import multiprocessing as mp

    t0 = time.time()
    with mp.Pool(processes=4) as pool:
        result_mp = pool.map(factorial, NUMBERS)
    t1 = time.time()
    print('Execution took {:.4f}'.format(t1 - t0))
    # Check memory usage
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage {current/1e6}MB; Peak: {peak/1e6}MB")
    print(f'Time elapsed: {time.time()-start_time:.2f}s')
    tracemalloc.stop()
