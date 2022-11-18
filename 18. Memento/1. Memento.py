"""
Whenever you have a change in a system you can return a token that gives you the snapshot of the current state,
so subsequently you can restore the system back to the state contained in snapshot
"""


class BankAccountSnapshot:  # Memento
    def __init__(self, balance):
        """Specify all the particulars(data) about the BankAccount in the particular moment in time"""
        self.balance = balance


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        """Returns a memento
        Takes a snapshot of the system in it's current state """
        self.balance += amount
        return BankAccountSnapshot(self.balance)

    def restore(self, memento: BankAccountSnapshot):
        self.balance = memento.balance  # since balance is the only thing we are storing

    def __str__(self):
        return f"Balance = {self.balance}"


if __name__ == '__main__':
    ba = BankAccount(100)  # BUT the problem is we do not have the memento for initial state
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)  # 175

    # restore to the m1 BankAccountSnapshot
    ba.restore(m1)
    print(ba)

    # restore to the m1 BankAccountSnapshot
    ba.restore(m2)
    print(ba)
