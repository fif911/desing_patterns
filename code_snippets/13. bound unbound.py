class Animal:
    """Animal class"""

    def __init__(self, name):
        """Initialize animal"""
        self.name = name

    def animal_name(self):  # bound_method
        """Return animal name"""
        return "This is a {}".format(self.name)

    def bound_method(self):  # bound_method
        pass

    @staticmethod
    def unbound_method():  # staticmethod is unbound_method
        pass


if __name__ == '__main__':
    Animal.animal_name  # will result in :
    # In python 2.0 <unbound method Animal.animal_name>
    # In 3 <function Animal.animal_name at 0x000001AB7F55FF70>
    #
    # Animal.animal_name() # will result in :
    # In 2.0 TypeError: unbound method animal_name() must be called with Animal instance as first argument (got nothing instead)
    # In 3 TypeError: animal_name() missing 1 required positional argument: 'self'
    """
    By providing ‘self’ as the first argument we are specifying that the methods within the
    class Animal are bound to the class instance, i.e, the first argument passed is itself the instance of a class.
    """
    print(Animal(
        "dog").animal_name)  # <bound method Animal.animal_name of <__main__.Animal object at 0x000001A1C971CA30>>
