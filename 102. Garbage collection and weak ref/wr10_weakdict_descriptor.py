"""
A descriptor as a class attr; only one is shared across all of the instances
But we want each instance to have it's own values
We can thus use a dict on the descriptor instance to keep track of per instance values using instance key
Ah but what if the instance goes away? should our dict continue to hold onto it ? 
"""

import weakref


class Age:
    """Age descriptor used as validator. Note: this is data descriptor"""

    def __init__(self):
        self.ages = weakref.WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.ages[instance]

    def __set__(self, instance, new_age):
        if new_age < 0:
            raise ValueError("age too low")
        if new_age > 120:
            raise ValueError("age too high")

        self.ages[instance] = new_age


class Person:
    def __init__(self, name):
        self.name = name

    age = Age()

    def __del__(self):
        print(f"Sadly, {self.name} is gone")
