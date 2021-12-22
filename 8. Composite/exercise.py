import unittest
from abc import ABC
from collections.abc import Iterable


class Summer(Iterable, ABC):
    @property
    def sum(self):
        sum_val = 0
        for obj_or_list in self:
            for num in obj_or_list:
                sum_val = sum_val + num
        return sum_val


class SingleValue(Summer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, Summer):
    pass


# if __name__ == '__main__':
#     sv = SingleValue(11)
#     for n in sv:
#         print(n + 1)


class Evaluate(unittest.TestCase):
    def test_exercise(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)

    def test_only_many_values(self):
        other_values = ManyValues()
        other_values.append(SingleValue(22))
        # other_values.append(22) # but this will fail
        # other_values.append(33) # but this will fail
        other_values.append(SingleValue(33))
        self.assertEqual(other_values.sum, 55)
