"""
Working with weakrefs .proxy
proxy allows us to treat weakref ust as regular object
"""
import weakref


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Dead {self.name}")


if __name__ == '__main__':
    p1 = Person('name1')
    p2 = weakref.proxy(p1)  # create a ref to existing object

    print(type(p2))  # <class 'weakproxy'>
    print(p2)
    print(p2.name)  # The proxy returns object; no () are needed

    del p1  # here we remove STRONG reference
    print(type(p2))  # <class 'weakproxy'>
    # print(p2) # tries to access object - raises: ReferenceError: weakly-referenced object no longer exists

