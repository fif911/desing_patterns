"""
The concept of the factory

it's essentially(по сути) the implementation of the idea of the Single resp principle
Once you have too many factories in the class it might make sense to move them out of the class or
at least group them somehow into separate entity (class)

and by using it we creating the relation between Point and Point Factory
"""

from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x=0, y=0):
        """
        By adding default params we can wiggle(извиваться) a bit from the depend between Point And PointFactory
        """
        self.y = y
        self.x = x

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    class PointFactory:
        """
        and by using it we creating the relation between Point and Point Factory

        And the main problem is discoverability. How does the client know that there is a factory now
        And the only thing you can do about it - you can specify the docs. That there is a PointFactory

        Also you can stick it as inner class. This is typically done in other programming languages like Java C#
        Not so much in Python but we can still do this

        ALSO WHEN Class is in class we can get rid of static method.
        (It was important to set them static if it's separate class)

        The only reason you may want to do it non static - if your factory also stores some states
        let's suppose when init with polar coords we want to store the bias of values of that point. and we want to
        add this value on init with polar point factory method
        """

        # @staticmethod
        # def new_cartesian_point(x, y):
        def new_cartesian_point(self, x, y):
            # And if we added default values we can init object let's say this way also
            p = Point()
            p.x = x
            p.y = y
            return p

        # @staticmethod
        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    # the cool thing - you can create instance of the PointFactory if you don't want to make them static but you
    # want to act factory in a static fashion
    factory = PointFactory()


if __name__ == '__main__':
    p = Point(2, 3)
    # using the point factory to init
    # p2 = PointFactory.new_polar_point(1, 2)
    # p2 = Point.PointFactory.new_polar_point(1, 2)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p, p2)
