#  one alternative to using a decorator is to use a Meta class
class Singleton(type):
    """ Metaclass that creates a Singleton base type when called. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        """Add the init to prove that it's not called twice"""
        print('Loading the DB')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
