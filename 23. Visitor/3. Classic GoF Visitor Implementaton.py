"""Simple numeric expression that we want to take in object-oriented format and work with them (print & evaluate)

There is no classic visitor, but we can think of a buffer object that is visiting
Classic implementation that works very well in statically typed languages

We see intrusive solution that goes against OCP
"""
from abc import ABC, abstractmethod
from typing import List, Union, Any
from multipledispatch import dispatch


class Expression(ABC):

    @abstractmethod
    def accept(self, visitor):
        """We want to force everyone to implement this method to ensure we would not have a runtime errors
        if type does not exist"""
        visitor.visit(self)


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        """Call 'visit' on self referring TO THE CORRECT TYPE"""
        visitor.visit(self)  # This visit will always go to DoubleExpression visit overloaded method


class AdditionExpression(Expression):
    def __init__(self, left: Union[DoubleExpression, Any], right: Union[DoubleExpression, Any]):
        self.left = left
        self.right = right

    def accept(self, visitor):
        visitor.visit(self)  # This visit will always go to AdditionExpression visit overloaded method


class SubtractionExpression(Expression):
    def accept(self, visitor):
        visitor.visit(self)  # I can assume that in statically typed languages, if you do this call to overloaded method
        # it will not compile as you want to use the overloaded function that does not exist
        # (dispatch for SubtractionExpression visit method does not exist)


class ExpressionPrinter:
    """Visitor that will have it's own buffer (unlike two previous examples)
    We want ExpressionPrinter to be able to take any kind of expression and be able to print it
    """

    def __init__(self):
        self.buffer = []

    @dispatch(DoubleExpression)
    def visit(self, de: DoubleExpression):
        self.buffer.append(str(de.value))

    @dispatch(AdditionExpression)
    def visit(self, ae: AdditionExpression):
        """Overloaded visit method
        This can be done using decorator
        Will be triggered when the expected types of arguments came
        """
        self.buffer.append('(')
        # TODO: We do not call it directly we call accept with which we may end up in any of the classes
        # and then in accept we call visitor referring already to the correct and definite class
        ae.left.accept(self)  # call accept and pass ExpressionPrinter (which is a visitor)
        self.buffer.append('+')
        ae.right.accept(self)
        self.buffer.append(')')

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == '__main__':
    # 1 + (2 + 3)
    e = AdditionExpression(DoubleExpression(1),
                           AdditionExpression(DoubleExpression(2), DoubleExpression(3))
                           )

    printer = ExpressionPrinter()
    printer.visit(e)
    print(printer)
