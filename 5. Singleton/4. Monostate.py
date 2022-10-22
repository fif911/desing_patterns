"""
This implementation stands apart from canonical implementation - mono state implementation.
We put all the state of the object into a static variable. But at the same time you allow people to create
new objects thereby(тем самым) making new instances which all access the same things

But this is not recommended approach. The better to use decorator or a metaclass
"""


class CEO:
    """
    only one CEO in the company. So people can call the init, construct the CEO but they always will be referencing
    the same CEO
    """
    __shared_state = {
        'name': 'Steve',
        'age': 21
    }

    def __init__(self):
        """
        When somebody will want to construct new CEO he always will be getting the same object

        KEY POINT: We are not copying data. We are copying reference. So when reference changes - every CEO changes
        """
        self.__dict__ = self.__shared_state  # assign the set of attributes to the shared state

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Monostate:
    """
    Making things more generic
    Inherit from this class if we want mono state implementation
    """
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money_managed = 0

    def __str__(self):
        return f'{self.name} manages ${self.money_managed}'


if __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 27
    print(ceo1)  # Steve is 27 years old

    print(ceo2)  # Steve is 27 years old

    print('--')

    ceo1 = CEO()
    print(ceo1)

    ceo1.age = 66

    ceo2 = CEO()
    ceo2.age = 77
    print(ceo1)
    print(ceo2)

    ceo2.name = 'Tim'

    ceo3 = CEO()
    print(ceo1, ceo2, ceo3)

    cfo1 = CFO()
    cfo1.name = 'Sheryl'
    cfo1.money_managed = 1

    print(cfo1)

    cfo2 = CFO()
    cfo2.name = 'Ruth'
    cfo2.money_managed = 10
    print(cfo1, cfo2, sep='\n')
