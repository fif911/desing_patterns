"""
Merge 2 ideas of events and properties

Property observer tell you whenever the property is actually changed

BUT There is a problem with this implementation
What happens when one property is dependent on another property?
"""


class Event(list):
    """List of functions that need to be invoked whenever this event happens"""

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObservable:
    """Inherit from this class and get a property changed event"""

    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, name, age=0):
        super().__init__()
        self.name = name
        self._age = age  # set inner age to param (as property uses 'age')

    # Build the getter and the setter
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            print(self._age)
            return  # as we do not really change anything
        self._age = value
        # call list of functions with name of property that has changed and new value
        self.property_changed('age', value)  # this is how you notify


class TrafficAuthority:
    """Monitor if person if allowed to drive based on age"""

    def __init__(self, person: Person):
        self.person = person
        # this is how we monitor
        person.property_changed.append(
            self.person_changed  #
        )

    def person_changed(self, property_name, new_value):
        """If age changed, check the new age. If they are too young - tell them; If they are old enough - notify them
        and stop monitoring"""
        print(f"{self.person.name} has turned {new_value}")
        if property_name == "age":
            if new_value < 16:
                print("Sorry you still cannot drive.")
            else:
                print('Okay, you can drive now.')
                self.person.property_changed.remove(
                    self.person_changed  # stop monitoring
                )
                print(f"We wont monitor you anymore, {self.person.name}")


if __name__ == '__main__':
    p = Person("John")
    ta = TrafficAuthority(p)
    for age in range(1, 20):
        print(f"Setting age to {age}")
        p.age = age
