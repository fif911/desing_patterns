"""
Every Person refers to central component (mediator) but they don't have any control over it
"""
import copy
from typing import List


class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []  # Chat log of this particular person
        self.room = None  # Will be assigned

    def receive(self, sender: str, message: str):
        """Person can receive a message"""
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat session][{self.room}] {s}")
        self.chat_log.append(s)

    def say(self, message):
        self.room.broadcast(self.name, message)

    def private_message(self, who: str, message: str):
        self.room.message(self.name, who, message)


class ChatRoom:
    idx = 1  # id tracker

    def __init__(self):
        self.people: List[Person] = []
        self._id = self.idx
        ChatRoom.idx += 1

    def join(self, person: Person):
        join_msg = f'{person.name} joins this room!'
        self.broadcast("Room", join_msg)
        person.room = self
        self.people.append(person)

    def leave(self, person: Person):
        leave_msg = f"{person.name} left."
        self.broadcast("Room", leave_msg)
        person.room = None
        self.people.remove(person)

    def broadcast(self, source: str, message: str):
        """Send message to everybody in the room except yourself"""
        for p in self.people:
            if p.name != source:
                p.receive(source, message)
        pass

    def message(self, source: str, destination: str, message: str):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)

    def __str__(self):
        return f"Room {self._id}"


if __name__ == '__main__':
    room = ChatRoom()
    john = Person('John')
    jane = Person('Jane')
    room.join(john)
    room.join(jane)

    john.say("Hi, room!")
    jane.say("Hey, John!")

    symon = Person('Symon')
    room.join(symon)
    symon.say('Hi everyone!')

    jane.private_message("Symon", "Glad you could join ;)")

    room.leave(john)

    room_loners = ChatRoom()

    ann = Person("Ann")
    room_loners.join(john)
    john.say("Is anybody here??")  # No one would receive this
    room_loners.join(ann)
    john.say("Heeeyyyy!")
    john.private_message("Ann", "Let's go private ;)")
    ann.private_message("John", "Ohhh. Nice to meet you ;)")
