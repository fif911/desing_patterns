"""
SO where should you use weakref ?
Great example: observer DP
in observes one or more objects register their interest in a central object
When the central obj state changes - it informs the observers what as happened
Weak references ensures - our observers isnt needlessly stopping objects from sticking around (не уходить,ошиваться )

Also weakrefs are perfect for caching:
- the cache doesnt prevent obj from removal
- but so long as the obj exists, it'll remain in the cache

Weakref based dicts
WeakKeyDictionary - the keys are weak refs and removed automatically
WeakValueDictionary - the values are weak refs and removed automatically
WeakSet - like a set, but the values are weak refs to other objects
"""
import weakref


class Person:
    def __init__(self, name):
        self.name = name
        self.observers = []

    def add_observers(self, *args):
        for new_observer in args:
            self.observers.append(weakref.ref(new_observer))

    def inform_observers(self, message):
        for one_observer in self.observers:
            if one_observer is None:
                continue
            print(f"Message for {one_observer().name}: {message}")
