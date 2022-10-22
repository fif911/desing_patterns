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

Takeaway: you will get the same instance in the result so db1==db2 BUT __init__ will be called twice
and that's typically now that we want
and that's cause __init__ is called immediately after __new__ doesnt matter what happens in __new__
"""
import random


class Database:
    initialized = False
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Define or redefine an allocator"""
        if not cls._instance:
            # call the parent __new__ method
            #  call to the base class constructor
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        This approach works unless we have nothing in init
        As init is called after new no matter what and you don't have any control of it
        """
        self.id = random.randint(1, 101)
        print('Generated an id of ', self.id)
        # id = random.randint(1, 101)
        # print('id =', id)
        # print("Loading a db from file")


database = Database()

if __name__ == '__main__':
    print(f"db({hex(id(database))}) id: {database.id}")
    d1 = Database()
    print(f"db({hex(id(database))}) id: {database.id}")
    d2 = Database()  # this is the reference to the same object as d1 But THE MAIN PROBLEM
    print(d1 == d2)  # True But it's only ok assuming you have nothing in the initializer cause as soon as you
    # start sticking thins into init you gonna see problems
    print(f"db({hex(id(database))}) id: {database.id}")
    print(f"db1 id: {d1.id}, db2 id: {d2.id}")
    print(database == d1)
    print(database == d2)

    print("\nHEX OF db1 and db2 are same as database")

    [print(hex(id(db))) for db in [database, d1, d2]]

"""
 THE MAIN PROBLEM:
 init is called twice unless we add some check
"""
