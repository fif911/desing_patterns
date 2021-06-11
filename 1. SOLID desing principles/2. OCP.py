# Open Closed principle
# OCP - open for extension, closed for modification
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    # by adding this function we violated open closed principle
    # so OCP says when you want to add new feature you add it via extension not via modification
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color: yield p


# as adding such functions violates OCP. We need to remake it and extend them
# Enterprise patterns. One of those called Specification. And that's what we need to implement here

class Specification:
    """
    Specification - class which determines whether or not particular item satisfies a particular criteria
    """

    def is_satisfied(self, item):
        """We will override this method"""
        pass

    def __and__(self, other):
        """binary and operator"""
        return AndSpecification(self, other)


class Filter:
    """
    The main idea you extend and inherit from this classes so we don't need to implement it here
    """

    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        """Receive arguments unlimited list of args"""
        self.args = args

    def is_satisfied(self, item):
        # map() goes through all the elements and applies lambda to it
        # all() check whether that every single argument is a boolean val of true
        # so if every spec is satisfied - combinator is satisfied
        """
        map() используется для применения функции к каждому элементу итерируемого объекта
        (например, списка или словаря) и возврата нового итератора для получения результатов
        map(lambda item: item[] expression, iterable)

         func = lambda x, y: x + y
         func(1, 2)
         3

         (lambda x, y: x + y)(1, 2)
         3

         func = lambda *args: args
         func(1, 2, 3, 4)
         (1, 2, 3, 4)
        """

        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    bf = BetterFilter()
    print('Green products (new):')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print('Large products')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    # Now let's implement the Size AND Color filter. And we can do it with Combinator.
    # Let's create an AndSpecification
    print('Large Blue items')
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    # we may want not to use AndSpec and it seems a bit long so we can override '&' sing to write:

    large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large AND blue')
