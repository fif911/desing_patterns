"""
The one of the simplest ways of implementing the Singleton is essentially(по сути) rewriting the allocator

Порядок: Сначала new потом init

What is the difference between __new__ and __init__ and when we should define each?
__new__ is an allocator, it basically allocates an object from scratch, and is the place where you can totally
substitute the object being created, as we do in the case of a Singleton Allocator. You want to have allocators
for things like caching, for example.

__init__ is where you initialize the object that has been constructed already. If this object doesn't have a
user-defined __new__, it is assumed that a new instance has been created and is available for you to customize.
__init__ is equivalent to the constructor in other programming languages.
"""
import random


class Database:
    initialized = False
    _instance = None

    def __init__(self):
        self.id = random.randint(1,101)
        print('Generated an id of ', self.id)
        # id = random.randint(1, 101)
        # print('id =', id)
        # print("Loading a db from file")
        pass

    def __new__(cls, *args, **kwargs):
        """Define or redefine an allocator"""
        if not cls._instance:
            # call the parent __new__ method
            #  call to the base class constructor
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


database = Database()

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()  # this is the reference to the same object as d1 But THE MAIN PROBLEM
    print(d1 == d2)  # True But it's only ok assuming you have nothing in the initializer cause as soon as you
    # start sticking thins into init you gonna see problems
    print(d1.id, d2.id)
    print(database == d1)

"""
 THE MAIN PROBLEM:
 init is called twice unless we add some check
"""
