"""
Builder facets. Sometimes you have an object that is so complicated to build that you need more than 1 builder to do it
So
1) how to have several builders for 1 object
2) how to make a nice fluent interface so you can jump from one builder to another
"""


class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, {self.city}\n' + \
               f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'


class PersonBuilder:
    """Base class builder"""

    def __init__(self, person=None):
        # def __init__(self, person=Person()):
        # self.person = person
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)  # provide an instance which is already being constructed

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    """Subclass for Job builder"""

    def __init__(self, person):  # We don't want to create person as we did in base builder
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    """Subclass for Adress builder"""

    def __init__(self, person):  # We don't want to create person as we did in base builder
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


"""
As all the builders  PersonAddressBuilder and PersonJobBuilder inherits from PersonBuilder they all have 
works and lives property so we can jump from one to another
"""
if __name__ == '__main__':
    pb = PersonBuilder()
    person = pb \
        .lives \
        .at('123 London') \
        .in_city('London') \
        .with_postcode('ADA131') \
        .works \
        .at('Fabricam') \
        .as_a('Engineer') \
        .earning(123000) \
        .build()
    print(person)
    print('---------------')
    person2 = PersonBuilder().build()
    print(person2)
