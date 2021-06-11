# Liskov substitution principle
# If you have some interface that takes some sort of base class you should be able to stick a derived (получений)
# class in there and everything should work
# Если в кусок кода приходит базовый клас parrent то в этот же кусок кода без каких либо помех может прийти
# любой его наследник

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    # making width and height as properties to show the particular kind of side effect braking the LSP using inheritance

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    """
    We can brake the LSP by making a derived class
    Class which inherits from rectangle which will break use_it method
    """

    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # and this breaks the LSP
    # setter for width
    @Rectangle.width.setter
    def width(self, value):
        # as width and height in square are equal when setting width we should also set the height
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width  # getting the rect width
    rc.height = 10  # setting the height to be 10. But in Square it's setting the width also! So w we cashed before
    # is no longer valid
    expected = int(w * 10)  # as we set height to 10 expect it to be 10
    print(f'Expected an area of {expected}, but got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

# Try to use square with use_it func

sq = Square(size=5)
use_it(sq)
# so the direct violation of LSP is that we now have an use_it fucntion which works with Rectangle but not works with
# child of it Square
