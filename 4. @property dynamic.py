class Item:
    def __init__(self, a, b):
        self.b = b
        self.a = a

    @property
    def area(self):
        return self.a * self.b


def lazy_property(fn):
    """
    Decorator that makes a property lazy-evaluated.
    """
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _lazy_property


class ItemWithHardCalculations:
    def __init__(self, a, b):
        self.b = b
        self.a = a

    @lazy_property
    def area(self):
        print("Calculated")
        return self.a * self.b

    def volume(self, height):
        # return self._lazy_area * height # also work but says that _lazy_area is undefined for this class
        return self.area * height


if __name__ == '__main__':
    item = Item(5, 10)  # item.area already calculated here
    print(item.__dict__)
    print(item.area)
    print(item.__dict__)
    item.a = 10
    print(item.area)

    lazy_item = ItemWithHardCalculations(15, 20)
    print(lazy_item.__dict__)
    print(lazy_item.area)
    print(lazy_item.__dict__)
    print(lazy_item.volume(2))
