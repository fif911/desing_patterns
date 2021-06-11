class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.id}:{self.name}'


class PersonFactory:
    id = 0
    inited = False

    # def create_person(self, name):
    #     p = Person(PersonFactory.id, name)
    #     PersonFactory.id += 1
    #     return p

    def create_person(self, name):
        if self.inited:
            self.id += 1
        else:
            self.inited = True

        return Person(self.id, name)


pf = PersonFactory()
print(pf.create_person('Alex'))
print(pf.create_person('Chris'))
