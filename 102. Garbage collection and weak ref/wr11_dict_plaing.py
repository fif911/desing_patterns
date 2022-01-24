import weakref


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"Sadly, {self.name} is gone")


if __name__ == '__main__':
    p1 = Person('name1')
    p2 = weakref.ref(p1)  # create a ref to existing object
    p3 = Person('name3')

    strong_ref_dict = {p1: 1, p3: 3}
    print(f"strong_ref_dict before deletion: {strong_ref_dict}")
    del p1
    print(f"strong_ref_dict after deletion: {strong_ref_dict}")  # p1 key is still in dict
