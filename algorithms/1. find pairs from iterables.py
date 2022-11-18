"""
Assignment
"""

from typing import Iterable, Tuple, Iterator, Generator


def find_pairs(target: int, iterable1: Iterable, iterable2: Iterable) -> Generator[Tuple[int, int]]:
    """ {General Description of the function}

    Generator that returns all unique pairs within iterables that add up to a certain target sum.

    Args:
        target: Value we are searching for
        iterable1: Iterable to search in
        iterable2: Iterable to search in

    Returns:
        Iterator with Tuples of pairs.
    """

    iterable1 = set(iterable1)
    iterable2 = set(iterable2)

    for i in iterable1:
        complement = target - i
        found = complement in iterable2

        if found:
            yield i, complement


# Example input:
if __name__ == '__main__':
    for answer in find_pairs(10, [1, 3, 3, 5, 7, 9], [3, 7, 7, 9]):
        print(answer)

# Would yield:
# (1, 9)
# (3, 7)
# (7, 3)
