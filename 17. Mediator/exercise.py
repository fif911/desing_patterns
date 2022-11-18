class Mediator:
    def __init__(self):
        self.people = []


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator

    def say(self, value):
        self.mediator.broadcast(self.name, value)

    def recieve(self, value):
        self.value += value
