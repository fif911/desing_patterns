"""
Working with weakrefs .ref

p2 = weakref.ref(p1)  # create a ref to existing object
print(p2().name)  # we need to invoke the weakref to get the object
"""

import weakref


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Dead {self.name}")


if __name__ == '__main__':
    p1 = Person('name1')
    p2 = weakref.ref(p1)  # create a ref to existing object

    print(p1.name)
    print(p2().name)  # we need to call the ref to get the object

    # what happens then target object dies
    del p1  # here we remove STRONG reference
    # p1 # NameError: name 'p1' is not defined
    print(p2() is None)  # now p2 is None
    # print(p2().name)  # AttributeError: 'NoneType' object has no attribute 'name'
