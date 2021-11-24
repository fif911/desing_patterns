"""
Purpose of the interface: we define list of methods that child Class have to implement

Interface Segregation
The idea is. Do not stick to many methods into an interface

Making interfaces which feature too many elements it's not a good idea
cause you forcing your clients to define methods( in this case) which they mind not even need. The ordinary printer does
not need to define fax and scan. And you don't fax and scan appear as code completion. So you should segregate
this things
"""

from abc import abstractmethod


class Machine:
    """
    Machine interface for multifunction printer
    """

    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    """
    The problem is if you want to make old printer
    As we have only ONE interface to work with you just into implementation of all this
    """

    def print(self, document):
        # OK
        pass

    def fax(self, document):
        """Old printer can't fax and scan. So what you do with this functions
        1) do nothing. But if the problem if you create a instance of OldFashionedPrinter - you still gonna see fax
        and scan as an interface member. And thay can think that fax method is dooing something. So they can end up
        calling fax method and there is absolutely no effect (cause of pass) and the client of our class gets a big
        surprise. Cause maybe they expected to send fax
        2) Raise error. It's something maybe is okay for small script but it's a big problem for much larger apps
        Cause people see the API and think OK maybe printer knows how to scan or fax
        SO ...... (below)
        """
        pass

    def scan(self, document):
        """
        Not supported!
        But still available in API SO ..... (below)
        """
        raise NotImplementedError('The printer can not scan')


"""
So the main idea of Interface aggregation - instead of having one big interface you want to have things granular
You want to split this interface in separate parts that people can implement

So the implementation is the following
"""


class Printer:  # it's interface
    @abstractmethod
    def print(self, document):
        pass


class Scanner:  # it's interface
    @abstractmethod
    def scan(self, document):
        pass


# and now we can combine the parts that we need
class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass


# But you can still create an interface with all these features so you should do this this way
class MultiFunctionDevice(Printer, Scanner):
    """
    Interface of the MultiFunctionDevice with print and pass methods
    """

    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    """
    You can just implement them functions like this
    Or you can use decorator principle (below)
    """

    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionMachineWithDecoratorPrinciple(MultiFunctionDevice):
    """
    If you already have printer and the scanner and you want to combine them somehow
    """

    def __init__(self, printer, scanner):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print()

    def scan(self, document):
        self.scanner.scan()
