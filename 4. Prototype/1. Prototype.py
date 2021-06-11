"""
When it's easier to copy an existing object to fully initialize a new one
Prototype - a partially or fully initialized object that you copy (clone) and make use of.

Idea is that we have existing design, we got a copy of this design, customize and use
- partially constructed
- fully constructed
"""
import copy


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


# john = Person('John', Address('123 Road', 'London', 'UK'))
# print(john)
# create new person who lives in the same place
# jane = john  # make copy BUT it's a reference assigment so 2 var are points at the same object
# jane.name = 'Jane'  # customize
# # but this will not going to work
# print(john)
# print(jane)
# Cause they referred to the same object
# Jane lives at 123 Road, London, UK
# Jane lives at 123 Road, London, UK

# also we can try doing it this way BUT when changing address as it still the same object it will change in 2 objects

# address = Address('123 Road', 'London', 'UK')
# john = Person('John', address)
# jane = Person('Jane', address)
# jane.address.street_address = "123B Road"
# print(john)
# print(jane)

# John lives at 123B Road, London, UK
# Jane lives at 123B Road, London, UK
# AND this is happening cause both objects are refer to the same address object (keep reference)
# and when reference is modified it modifies everywhere

# and this should be done using deep copy.
# It's performs a recursive copy of all of the attributes of an object
john = Person('John', Address('123 Road', 'London', 'UK'))
jane = copy.deepcopy(john)  # now it's separate object not in any way referring to john
# jane = copy.copy(john)  # Shallow copy so any obj that is reference just gets copied as a reference
# so jane refers to the same address as John
# will change name correctly and address for both
jane.name = 'Jane'
jane.address.street_address = '123B Road'
print(john)
print(jane)
