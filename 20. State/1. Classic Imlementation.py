"""
Bizarre implementation

Light on / off switch
Classic example from the book. Not so practical
"""
from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()  # Handle current switch state

    def turn_on(self):
        """Whenever wer want to flick switch we do not do it directly
        we do not modify state directly
        we use stored state and call a transition on it. So we call on function ON A stored state"""
        self.state.on(self)

    def turn_off(self):
        self.state.off(self)


class State(ABC):  # Base class
    def on(self, switch: Switch):
        print("Light is already on")

    def off(self, switch: Switch):
        print("Light is already off")


class OnState(State):
    def __init__(self):
        print("Light is turned on")

    def off(self, switch):
        print("Turning light off")
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print("Light is turned off")

    def on(self, switch: Switch):
        print("Turning light on")
        switch.state = OnState()


if __name__ == '__main__':
    sw = Switch()
    sw.turn_on()
    sw.turn_off()
    sw.turn_off()
