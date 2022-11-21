import unittest
from enum import Enum
from typing import List, Union


class LockState(str, Enum):
    LOCKED = 'LOCKED'
    OPEN = 'OPEN'
    ERROR = 'ERROR'


class CombinationLock:

    def __init__(self, combination: List[int]):
        self.status: Union[LockState, List[int]] = LockState.LOCKED
        self.combination = "".join([str(x) for x in combination])

    def reset(self):
        self.status = LockState.LOCKED

    def enter_digit(self, digit):
        digit = str(digit)

        if self.status == "LOCKED":
            self.status = digit

        elif self.status not in list(LockState):
            self.status += digit

            if self.status == self.combination:
                self.status = LockState.OPEN
            elif len(self.status) >= len(self.combination):
                self.status = LockState.ERROR


class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)
