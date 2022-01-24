"""
Output
before loop
after loop, ending program # Printed before objects die
Dead Name : 0
Dead Name : 1
Dead Name : 2

Process finished with exit code 0

since all_people list is global var - all_people list and it's elements persons only released then program exits
And this is despite the fact than no Person object was ever assigned to a variable!

WHICH MEANS if you will not clean up things in your global list  - you gonna have Memory leak !
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Dead {self.name}")


if __name__ == '__main__':
    all_people = []  # since its global var - all_people and it's elements persons only released then program exits
    print("before loop")
    for i in range(3):
        all_people.append(Person(f"Name : {i}"))
    print("after loop, ending program")
