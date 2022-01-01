"""
The typical example of Command DP is Bank account example
"""
from abc import ABC
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, "
              f"balance = {self.balance}")

    def withdraw(self, amount):
        """A little bit more complex cause we need to make sure person is not going over the overdraft"""
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, "
                  f"balance = {self.balance}")
            return True
        return False

    def __str__(self):
        return f"Balance = {self.balance}"


# Rn you can work with BankAccount and you dont need Command. You can deposit and withdraw money
# and everything will work
# lets imagine we are working with a real bank
# Every bank needs to take a record of every transaction that is going on
# So if you just call these methods there is not record anywhere that they were actually invoked
# so you can provide sort of interface for calling commands

# define a interface
# (that's not strictly necessary cause we are in Python and everything works on DuckTyping)
# but that's good idea cause it sets your expectations on the board of command can do it

class Command(ABC):
    def invoke(self):
        # we not using __call__ to make explicit that we calling invoke method by .
        pass

    def undo(self):
        """
        Rolls back the command
        """
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 1
        WITHDRAW = 2

    def __init__(self, account, action, amount):
        """
        We initing command with all the info needed to perform operation and yo undo it

        :param account: What account to operate on
        :param action: it's up to you how to implement this. Easily to put in Enum
        :param amount:
        """
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None
        super().invoke()

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True

        elif self.action == self.Action.WITHDRAW:
            # we dont really know whether withdrawal will work or not
            # and we need to go back and modify it to return status
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        # the side effect of Command that you can implement undo operations right inside the command
        # However this particular implementation, if you decide to do undo is going to change pretty much everything
        # that we do around BankAccountCommand:
        # we try to be symmetric. If you want to undo deposit. You undo a deposit my making a withdraw
        # that's not strictly speaking the most correct way of undoing back account operations

        # We need to make sure that we undo only succeeded operations
        if not self.success:
            return

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)
        # and this seems like correct code BUT lets show how it all can go wrong


if __name__ == '__main__':
    ba = BankAccount()  # 0$
    # instead of staring using it. We will create BackAccountCommand

    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    cmd.invoke()
    print(f"After $100 deposit: {ba}")

    cmd.undo()
    print(f"$100 deposit undone: {ba}")
    # BUT lets show how it all can go wrong
    # letst do illegal command

    illegal_command = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
    illegal_command.invoke()
    print(f"After impossible withdraw: {ba}")
    illegal_command.undo()  # This will deposit a 1000$ !
    print(f"After undo impossible withdraw: {ba}")
    # and it tells us one thing - we need to track whether or not a perticular operation has in fact succeed
    # add success flag
