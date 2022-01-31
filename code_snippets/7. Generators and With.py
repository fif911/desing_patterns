# https://realpython.com/introduction-to-python-generators/
# 4. Pipelining Generators
from contextlib import contextmanager
from timeit import timeit

from PIL.ImImagePlugin import number


def generator_with_return(nums):
    # this returns generator in any case. So we should not combine them
    if len(nums) == 1 or len(nums) == 0:
        print("return 'hey'")
        return ["Hey"]
    for _ in nums:
        yield _ * 1000


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


# Advanced Generator Methods
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1


@contextmanager
def function_based_context_manager():
    print("Entering the context...")
    yield "Hello, World!"
    print("Leaving the context...")


if __name__ == '__main__':
    # 4. Pipelining Generators
    print(list(square(fibonacci_numbers(10))))
    print(list(fibonacci_numbers(10)))
    print(sum(square(fibonacci_numbers(10))))
    print(timeit('list(square(fibonacci_numbers(10)))',
                 setup="from __main__ import square,fibonacci_numbers",
                 number=10000))

    # Advanced Generator Methods
    print("Advanced Generator Methods")
    pal_gen = infinite_palindromes()
    next(pal_gen)
    pal_gen.send(50)
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        if digits == 5:
            try:
                pal_gen.throw(ValueError('We do not like large palindromes'))  # returns ValueError
            except ValueError:
                pass
        # pal_gen.send(10 ** (digits))

    with function_based_context_manager() as hello:
        print(hello)
