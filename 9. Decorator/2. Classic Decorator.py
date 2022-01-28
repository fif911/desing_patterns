"""
THe most classic decorator implementation is when u build a class that kind of augments the
functionality of the existing class.

And we are able to add functionality to a class IN RUNTIME !!!!
"""
from abc import ABC


class Shape(ABC):
    """This class does not have a lot in it. Without concrete implementations
    BTW this base class business is not necessary. But im doing it for completeness"""

    def __str__(self):
        return ""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"A circle of radius {self.radius}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"A square with side {self.side}"


class ColoredShape(Shape):
    """
    Note we cant inherit it from square or circle cause it have to work with both square and circle
    THIS IS DECORATOR CLASS
    It adds the functionality on top of the existing class without inheriting from it
    """

    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception("Cannot apply same decorator twice")
        self.color = color
        self.shape = shape

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.transparency = transparency
        self.shape = shape

    def __str__(self):
        return f"{self.shape} has {self.transparency * 100.0}% transparency"


if __name__ == '__main__':
    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape(circle, "red")
    print(red_circle)
    # and also you can combine several decorators on top of the particular class
    red_half_transparent_circle = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_circle)
    # also nothing prevents u from applying the same decorator twice

    mixed = ColoredShape(ColoredShape(Square(3), "red"), "blue")
    print(mixed)
    # maybe thats not what you want so you can prevent from doing so by altering __init__ method ...

    # What you can do you can apply
    # ColoredShape(TransparentShape(ColoredShape that's currently will not be caught and its actually
    # very difficult to catch if you want to handle this kinds of situations

    # The problem is the decorator doesnt allow u to access underlying object
    # Which means we cannot actually use the resize method of the Circle on the Decorated Shape
    circle.resize(2)
    # red_circle.resize()  # will not work
    # cause ColoredShape Is a Shape and not a Circle so it does not have resize method and we can call it
