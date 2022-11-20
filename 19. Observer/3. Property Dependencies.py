"""
BUT There is a problem with Property Observer implementation
What happens when one property is dependent on another property?

We want to monitor when person can vote. But there is no setter
@property
def can_vote(self):
    Problem

    This property does not have setter obviously
    SOOOO How do we send notifications on changes in voting ability of a person
    return self._age >= 18

But this approach is really does not scale

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

        # cache can vote value, set the notification for it only when can vote has changed
        old_can_vote = self.can_vote  # But this does not really scale as we need to store all the old values here

        self._age = value
        # call list of functions with name of property that has changed and new value
        self.property_changed('age', value)  # this is how you notify

        if old_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)  # Invoke notification Event only of can_vote has changed

    @property
    def can_vote(self):
        """ Problem
        This property does not have setter obviously
        SOOOO How do we send notifications on changes in voting ability of a person"""
        return self._age >= 18


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
    def person_changed(name, value):
        """Check if voting status has changed"""
        if name == "can_vote":
            print(f"Voting ability changed to {value}")


    p = Person("John")
    p.property_changed.append(
        person_changed
    )

    ta = TrafficAuthority(p)
    for age in range(1, 22):
        print(f"Setting age to {age}")
        p.age = age
