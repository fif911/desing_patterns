"""
You can specify that a func should be called when the weakref's referent goes away (object it refers to)
this func gets the weakref obj as argument
but the referent has already disappeared so you cannot get any last minute data from it

Before deleting: p2.name= name1
Deleting
Dead name1 # this is from __del__ (dunder del)
Boo hoo: weakref obj 1585122638800 is refless! # this is from the callback
Done deleting


"""

import weakref


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Dead {self.name}")


def value_gone(ref):
    """Invoke the callback when the referent disappears"""
    print(f"Boo hoo: weakref obj {id(ref)} is refless!")


if __name__ == '__main__':
    p1 = Person('name1')
    p2 = weakref.proxy(p1, value_gone)  # create a ref to existing object with callback

    print("Before deleting: p2.name=", p2.name)  # The proxy returns object; no () are needed
    print("Deleting")
    del p1  # here we remove STRONG reference
    print("Done deleting")
