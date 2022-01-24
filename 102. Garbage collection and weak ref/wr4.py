"""
Output:
--------0---------
Dead Name : 2 # all local vars go away when function returns
Dead Name : 1
Dead Name : 0
--------1---------
Dead Name : 2
Dead Name : 1
Dead Name : 0

Process finished with exit code 0

One solution is Local vars
- they go away when function exits

"""
import gc


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Dead {self.name}")


def create_some_people():
    all_people = []

    for i in range(3):
        all_people.append(Person(f"Name : {i}"))
    # all local vars go away when function returns


if __name__ == '__main__':
    for i in range(2):
        print(f"--------{i}---------")
        create_some_people()

    print("finish")