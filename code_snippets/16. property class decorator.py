"""
property name in Python is a class!!!

Remember, that the @decorator syntax is just syntactic sugar; the syntax:
@property
def foo(self): return self._foo

really means the same thing as:
def foo(self): return self._foo
foo = property(foo)

Last but not least, the property object acts as a descriptor object, so it has .__get__(), .__set__() and .__delete__()
methods to hook into instance attribute getting, setting and deleting:
"""


#     Typical use is to define a managed attribute x:

class C(object):
    def getx(self): return self._x

    def setx(self, value): self._x = value

    def delx(self): del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")  # THIS IS descriptor class by fact !. property its a class
    # that with params able to implement descriptor protocol


#     Decorators make defining new properties or modifying existing ones easy:
class ClassP(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


if __name__ == '__main__':
    property_descriptor = property()

    print(property_descriptor)  # returns descriptor object
