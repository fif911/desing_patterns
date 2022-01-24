"""
The another solution - use weak references
before loop
Dead Name : 0
Dead Name : 1
Dead Name : 2
[<weakref at 0x000001FB1E95C310; dead>, <weakref at 0x000001FB1EC1C9F0; dead>, <weakref at 0x000001FB1EC20BD0; dead>]
after loop, ending program

Process finished with exit code 0

all_people still global variable
we created weakref to obj in list. so ref count is 0 and it's collected by gc
"""
import weakref


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Dead {self.name}")


if __name__ == '__main__':
    all_people = []
    print("before loop")
    for i in range(3):
        all_people.append(weakref.ref(Person(f"Name : {i}")))  # create a weakref to an object
        # which means if we are the only thing standing between object getting garbage collected or not -
        # then we not gonna stop it

    print(all_people)
    print("after loop, ending program")
