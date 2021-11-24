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

# The next if covered in 2. Factory.py file

# For SPR we can move Factories to another class
class PointNew:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return PointNew(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        # this is not actually a polar point. It just gets initializing differently
        return PointNew(rho * cos(theta), rho * sin(theta))


# but here goes the problem with discoverability. We can specify that there is a factory in docs BUT also we
# can move the class in class in Python

class PointNewWithInternalFactory:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    class PointFactory:
        # they are not longer need to be static but may be (if not static - self have to be added)
        # @staticmethod
        # also non static method allows us to use some internal object stored values for new object creation
        def new_cartesian_point(self, x, y):
            return PointNewWithInternalFactory(x, y)

        def new_polar_point(self, rho, theta):
            # this is not actually a polar point. It just gets initializing differently
            return PointNewWithInternalFactory(rho * cos(theta), rho * sin(theta))

    # If we do not want to make factory method static but we want them to act in a static fashion
    # also we can make an instance of  PointFactory (kind of a singleton)
    factory = PointFactory()


if __name__ == '__main__':
    # In python we can't shield people from using default init approach but what they can do - they can
    # use factory methods
    p = Point(2, 3)
    p2 = Point.new_polar_point(1, 2)
    print(p, p2)

    p1 = PointNewWithInternalFactory.factory.new_polar_point(1, 3)
    print(p1)
