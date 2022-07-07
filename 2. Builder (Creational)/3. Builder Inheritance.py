"""
in 2. Builder Facets we directly violate OCP as to add a new builder we need to edit the Base builder
And there is an alternative way to use inheritance
When you want to build up the additional information you inherit from a builder that you already got
"""


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as {self.position}.'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


# continue inheriting to make new functionality
class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    # use the most derived builder
    pb = PersonBirthDateBuilder()
    me = pb \
        .called('Dmitri') \
        .works_as_a('quant') \
        .born('1/1/1980') \
        .build()  # this does NOT work in C#/C++/Java/...
    print(me)
    person2 = PersonBirthDateBuilder().build()
    print(person2)
