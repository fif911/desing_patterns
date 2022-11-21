"""
Original implementation is using switch statements, but we will simulate it with if

Works well with small state machines
"""
from enum import Enum, auto


class State(Enum):
    LOCKED = auto()
    FAILED = auto()
    UNLOCKED = auto()


if __name__ == '__main__':
    # This approach does not use any additional data structures
    code = '1234'  # right code to enter
    state = State.LOCKED
    entry = ''  # code that already typed

    while True:
        if state == State.LOCKED:
            entry += input(entry)

            if entry == code:
                state = State.UNLOCKED
            if not code.startswith(entry):
                state = State.FAILED
        elif state == State.FAILED:
            print("\nFailed")
            entry = ''
            state = state.LOCKED
        elif state == state.UNLOCKED:
            print("\nUNLOCKED")
            break  # unlocked so exit
