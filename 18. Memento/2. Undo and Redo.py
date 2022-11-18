"""
Whenever you have a change in a system you can return a token that gives you the snapshot of the current state,
so subsequently you can restore the system back to the state contained in snapshot

Storing all the sequence of mementos can be costly. But there are situations where you can do it
"""
from typing import List


class BankAccountSnapshot:  # Memento
    def __init__(self, balance):
        """Specify all the particulars(data) about the BankAccount in the particular moment in time"""
        self.balance = balance


class BankAccount:

    def __init__(self, balance):
        self.balance = balance
        self.changes: List[BankAccountSnapshot] = [BankAccountSnapshot(self.balance)]
        self.current = 0  # pointer to where in the list of mementos we are right now

    def deposit(self, amount):
        """Returns a memento
        Takes a snapshot of the system in it's current state """
        self.balance += amount

        m = BankAccountSnapshot(self.balance)
        self.changes.append(m)
        self.current += 1
        return m

    def restore(self, memento: BankAccountSnapshot):
        if memento:  # Guarding condition if memento is None
            self.balance = memento.balance  # since balance is the only thing we are storing
            self.changes.append(memento)
            self.current = len(self.changes) - 1  # point to the last element in the list

    def undo(self):
        if self.current > 0:
            self.current -= 1
            m: BankAccountSnapshot = self.changes[self.current]
            self.balance = m.balance
            return m  # return memento that we have moved back to

        print("Cannot undo initial state")
        return None

    def redo(self):
        if self.current + 1 < len(self.changes):
            self.current += 1
            m: BankAccountSnapshot = self.changes[self.current]
            self.balance = m.balance
            return m  # return memento that we have moved forward to
        print("Cannot move forward further")
        return None

    def __str__(self):
        return f"Balance = {self.balance}"


if __name__ == '__main__':
    ba = BankAccount(100)  # BUT the problem is we do not have the memento for initial state
    ba.deposit(50)
    ba.deposit(25)
    print(ba)  # 175

    ba.undo()
    print(f"Undo1: {ba}")

    ba.undo()
    print(f"Undo2 (go to original state): {ba}")

    ba.undo()
    print(f"Undo3: (Try to go further but not possible) {ba}")

    ba.redo()
    print(f"Redo1: {ba}")

    ba.redo()
    print(f"Redo2: {ba}")

    ba.redo()
    print(f"Redo3: {ba}")
