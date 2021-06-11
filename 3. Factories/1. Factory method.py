"""
IN modern naming - factory method is typically any method which creates an object.
By fact it's alternative to init that and have lots of advantages (good naming)

cause big init it's kind of God object but for initializer

Scenario:

We have class point and we want to init it with 2 points x & y in cartesion system
Imagine you want to init it with polar coordinates
Redeclaration of init is impossible
- we can expand the initializer. But this requires a lot of changes.
            1) Need to introduce some sort of indicator which system coordinates you want - enum
            2) make a,b cause we may be passing x and y or rho and theta

....


"""
from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # this will not work
    # def __init__(self, rho, theta):

    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     """
    #     This solution is pretty painful. If you need to introduce another coor system you will have to change the Enum
    #     and also you will need to add another if check. What kind of brakes the OCP. Also the problem -
    #     vars are called
    #     a,b and client have somehow to figure out that a maps to x and b maps to y
    #     """
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * sin(b)
    #         self.y = a * cos(b)

    # Factory method allows us to be explicit (явный) about what kind of Point we initializing
    # And it's a lot more understandable. Namings are correct
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        # this is not actually a polar point. It just gets initializing differently
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    # In python we can't shield people from using default init approach but what they can do - they can
    # use factory methods
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)
