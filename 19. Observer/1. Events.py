"""
Event something that happens, and you want to have notification when something happens
"""


class Event(list):
    """List of functions that need to be invoked whenever this event happens"""

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Person:
    def __init__(self, name, address):
        self.address = address
        self.name = name
        self.false_ill = Event()  # event to which others can subscribe

    def catch_a_cold(self):
        self.false_ill(self.name, self.address)  # we call event with all subscribed functions


def call_doctor(name, address):
    # we call doctor for a given name and address
    print(f"{name} needs a doctor at {address}")


if __name__ == '__main__':
    person = Person("Sherlock", '221B Baker St')
    person.false_ill.append(
        lambda name, address: print(f"{name} is ill.")  # we have subscribe with lambdas
    )
    person.false_ill.append(call_doctor)  # person might fall ill, and if they fall ill, we want to call a doctor

    person.catch_a_cold()

    # we can remove listener if we no longer want to call a doctor
    person.false_ill.remove(call_doctor)

    person.catch_a_cold()