"""OUTPUT:
[{'__name__': '__main__',... 'Person': <class '__main__.Person'>, 'p1': <__main__.Person object at 0x00000198CF220FD0>}]
Dead name1 # on program end
"""

import gc


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        """NOT A DESTRUCTOR
        this method is invoked just before an object is about to be released

        this is not something you should normally use. A lot of warnings on it
        its the closest thing to destructor Python has, but its not one
        """
        print(f"Dead {self.name}")


if __name__ == '__main__':
    p1 = Person("name1")
    print(gc.get_referrers(p1))  # result is list with 1 dict in it. [{...}]  in dict we will find Person class
    # the reason why we getting dict - p1 is a global var.
    # Global vars are stored in dict which we can access by globals() func
    # WHICH MEANS - once we define a global var - there is at least one reference to it until the program exits
    # - global variables never go away on their own
    # - elements of global containers do not either !

    # and right after we add __del__ FOR SOME REASON __del__ method called
    # and THE ANSWER IS: actually __del__ called when program exits.
    # when program exits - all vars are deleted and all obj go away
    # (The reference can be from var but also from another data structure) when ref count >= 1 - obj stays alive
