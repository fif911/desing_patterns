from unittest import TestCase, main
from copy import deepcopy



def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    x = factory()
    y = factory()
    return x is y


class Evaluate(TestCase):
    def test_exercise(self):
        obj = [1, 2, 3]
        self.assertTrue(is_singleton(lambda: obj))
        self.assertFalse(is_singleton(lambda: deepcopy(obj)))
        self.assertFalse(is_singleton(lambda: deepcopy(obj)))
        self.assertFalse(is_singleton(lambda: [1, 2, 3]))
        self.assertFalse(is_singleton(lambda: [1, 2, 3, 4]))


if __name__ == '__main__':
    main()
