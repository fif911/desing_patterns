"""
method of accessing attributes, moving property behavior to external implementation.
Descriptors are Python objects that implement a method of the descriptor protocol,
which gives you the ability to create objects that have special behavior when they're accessed as attributes of other objects
Desc is an instance of an object that is attached to another class.
Allow us to simulate attr access with functions instead

https://www.youtube.com/watch?v=ZdvpNaWwx24&t=519s
"""


# named_descriptors
class MyDescriptor(object):
    def __init__(self, field=""):
        self.field = field

    def __get__(self, obj, type):
        print("Called __get__")
        return obj.__dict__.get(self.field)

    def __set__(self, obj, val):
        print("Called __set__")
        obj.__dict__[self.field] = val


def named_descriptors(klass):
    for name, attr in klass.__dict__.items():
        if isinstance(attr, MyDescriptor):
            attr.field = name
    return klass


@named_descriptors
class MyClass(object):
    x = MyDescriptor()


# END named_descriptors


# validator desr example
class Descriptor(object):

    def __init__(self, name=''):
        self.name = name

    def __get__(self, obj, objtype):
        return "{}for{}".format(self.name, self.name)

    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")


class GFG(object):
    """usage:
    g = GFG()
    print(g.name)  # for
    g.name = "Computer"  # ComputerforComputer
    print(g.name)
    """
    name = Descriptor()


# validator desr example

# class BankTransaction(object):
#     before = CurrencyField(0)
#     after = CurrencyField(0)
#
#     def __init__(self, account, before, after):
#         self.account = account
#         self.before = before
#         self.after = after


if __name__ == '__main__':
    g = GFG()
    print(g.name)  # for
    g.name = "Computer"  # ComputerforComputer
    print(g.name)
    try:
        g.name = 213
    except TypeError as e:
        print('g.name = 213')
        print(f'TypeError: {e}')  # specified in __set__
