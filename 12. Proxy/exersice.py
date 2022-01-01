class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    @property
    def age(self):
        return self.person.age

    @age.setter
    def age(self, value):
        self.person.age = value

    def drink(self):
        if self.person.age < 18:
            return "too young"
        return self.person.drink()

    def drive(self):
        if self.person.age < 16:
            return "too young"
        return 'driving'

    def drink_and_drive(self):
        return 'dead'
