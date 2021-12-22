"""
Multi user have
"""
import random
import string
import sys
import time
from pympler import asizeof, tracker, classtracker


class User:
    def __init__(self, name):
        self.name = name  # full name of the person
        # josh doe josh smith, mary smith
        # so putting this values in same string not the best idea


class User2:
    """Class with all the common first and last names"""
    strings = []

    def __init__(self, fullname):  # name = full name
        # split into 2 and store indices

        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x)
                      for x in fullname.split()]

    def __str__(self):
        return " ".join([self.strings[x] for x in range(len(self.strings))])


def random_string():
    """func to emulate peoples names"""
    chars = string.ascii_lowercase
    return ''.join(
        [random.choice(chars) for x in range(3)]
    )


if __name__ == '__main__':
    s_tr = tracker.SummaryTracker()
    tr = classtracker.ClassTracker()
    tr.track_class(User)
    tr.track_class(User2)
    tr.create_snapshot()
    users = []

    number = 5*10000
    first_names = [random_string() for x in range(number)]
    last_names = [random_string() for x in range(number)]

    start = time.time()
    for first, last in zip(first_names, last_names):
        users.append(User(f'{first} {last}'))  # this is going to work But it will waste a lot of memory
    print(f"First loop took us: {time.time() - start}")
    print(f"Size of list in b: {asizeof.asizeof(users)}")
    tr.create_snapshot()

    # there is only 200 unique strings
    # so we should not waste 100 * 100 = 10 000 pieces of memory

    u2 = User2('Jim Jones')
    u3 = User2('Frank Jones')
    print(u2.names)
    print(u3.names)
    print(User2.strings)

    users2 = []

    start = time.time()
    for first, last in zip(first_names, last_names):
        users2.append(User2(f'{first} {last}'))
    print(f"Second loop took us: {time.time() - start}")
    print(f"Size of list in b: {asizeof.asizeof(users2)}")
    tr.create_snapshot()

    print(f"len(User2.strings): {len(User2.strings)}")

    s_tr.print_diff()
    print()
    tr.stats.print_summary()
