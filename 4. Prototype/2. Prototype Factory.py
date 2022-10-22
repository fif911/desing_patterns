"""
Quite often it's inconvenient(неудобно) to keep making those copies manually. For ex if you have a few predefined
prototypes in your entire application it would be nice to pack them into a factory and then provide factory methods
so nobody has to take a prototype and perform the deep copy and customization by hand
It's much easier to wrap it into separate component

The take away:
When you have a fixed number of prototypes in your system you can put them into factory. and then create a factory
methods so that the construction of copies of those prototypes is even easier
"""

import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite  # position where smb works (апартаменты)
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


# we want to make Employees  to work in offices suite is office id
class EmployeeFactory:
    # Prototypes for objects
    main_office_employee = Employee('', Address('123 East Drive', 0, 'London'))
    aux_office_employee = Employee('', Address('123B East Drive', 0, 'London'))  # auxiliary (вспомогательный)

    @staticmethod
    def __new_employee(prototype, name, suite):
        """As 2 factory methods below are just taking prototypes and customizing them
        __ - static method that not should be used from outside"""
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite = suite # set value for internal object
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


# main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
# aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

# john = copy.deepcopy(main_office_employee)
# john.name = "John"
# john.address.suite = 101
# print(john)

# would prefer to write just one line of code
john = EmployeeFactory.new_main_office_employee('John', 213)
jane = EmployeeFactory.new_aux_office_employee('Jane', 500)
print(john, '\n', jane)
