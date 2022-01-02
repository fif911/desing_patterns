"""
Composite command (also called as macros)

If you think about typical operation involving 2 parties
e.g. transferring money from one bank account from another and undoing this operation

How we can do this ?
On the one hand we can do 2 commands. But that's not good cause of possible failure

"""
import unittest
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
    def __init__(self):
        self.success = False

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
        super().__init__()  # we need to do a super class call to define success flag
        self.amount = amount
        self.action = action
        self.account = account
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


class CompositeBankAccountCommand(Command, list):
    """
    List of commands that also a command
    (that's composite DP)
    """

    def __init__(self, items=[]):
        super().__init__()  # call the base class to init the whole thing

        for command in items:
            self.append(command)

    def invoke(self):
        for command in self:
            command.invoke()

    def undo(self):
        for command in self:
            command.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct, to_acct, amount):
        super().__init__([
            BankAccountCommand(from_acct,
                               BankAccountCommand.Action.WITHDRAW,
                               amount),
            BankAccountCommand(to_acct,
                               BankAccountCommand.Action.DEPOSIT,
                               amount)
        ])

    def invoke(self):
        ok = True  # flag that defines whether the previous command succeeded
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False  # something failed and we mark all next commands as failed
                # (the failed one is already marked)
        self.success = ok


class TestSuit(unittest.TestCase):
    # def test_composite_deposit(self):
    #     # we want to make 2 deposit but with single command
    #     ba = BankAccount()
    #     deposit1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    #     deposit2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 50)
    #
    #     composite = CompositeBankAccountCommand([deposit1, deposit2])
    #     composite.invoke()
    #     print(ba)
    #     composite.undo()
    #     print(ba)
    #
    # def test_transfer_fail(self):
    #     """
    #     The problem with this test is when we try to transfer too much money
    #     Success of one command should be tied to success of another. And when it's not
    #     Implemented yet. Transferring too much money will fail with command of withdrawal
    #     But will succeed on deposit
    #
    #     So if operation fail. We should not perform next one (and set next as also failed)
    #
    #     To fix it we need to come back to our definition of Command and give it attribute of success
    #
    #     And lets make a new command. Money transfer command,
    #     which would be a bit more sophisticated(сложный) than CompositeBankAccountCommand
    #     """
    #     print()
    #     ba1 = BankAccount(100)
    #     ba2 = BankAccount(0)
    #
    #     amount = 1000
    #     wc = BankAccountCommand(  # withdrawal command
    #         ba1, BankAccountCommand.Action.WITHDRAW, amount
    #     )
    #     dc = BankAccountCommand(  # deposit command
    #         ba2, BankAccountCommand.Action.DEPOSIT, amount
    #     )
    #     transfer = CompositeBankAccountCommand([wc, dc])
    #
    #     print("Before invocation")
    #     transfer.invoke()
    #     print("transfer.invoke():", f"ba1 = {ba1}; ba2 = {ba2}", sep=".........")
    #     transfer.undo()
    #     print("transfer.undo():", f"ba1 = {ba1}; ba2 = {ba2}", sep=".........")

    def test_better_transfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount(0)

        # amount = 100
        amount = 1000

        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print("transfer.invoke():", f"ba1 = {ba1}; ba2 = {ba2}", sep=".........")
        transfer.undo()
        print("transfer.undo():", f"ba1 = {ba1}; ba2 = {ba2}", sep=".........")
        print(f"transfer.success = {transfer.success}")


if __name__ == '__main__':
    unittest.main()
