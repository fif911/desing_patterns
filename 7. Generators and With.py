# 4. Pipelining Generators
from timeit import timeit

from PIL.ImImagePlugin import number


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


if __name__ == '__main__':
    # 4. Pipelining Generators
    print(list(square(fibonacci_numbers(10))))
    print(list(fibonacci_numbers(10)))
    print(sum(square(fibonacci_numbers(10))))
    print(timeit('list(square(fibonacci_numbers(10)))',
                 setup="from __main__ import square,fibonacci_numbers",
                 number=10000))
