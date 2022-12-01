"""
Classic implementation works very well in statically typed languages

Implementation of accept is not required

The problem of not doing accept is that if you forget to implement one - the program would not crash and will work
due to duck-typing

But if you add one more class and do not add one more overloaded method for this class - you will end up with
It will fail with:
    raise NotImplementedError('Could not find signature for %s: <%s>' %
NotImplementedError: Could not find signature for visit: <SubtractionExpression>
"""

from abc import ABC
from typing import List, Union, Any
from multipledispatch import dispatch


class Expression(ABC):

    def accept(self, visitor):
        visitor.visit(self)


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left: Union[DoubleExpression, Any], right: Union[DoubleExpression, Any]):
        self.left = left
        self.right = right


class SubtractionExpression(Expression):
    def __init__(self, left: Union[DoubleExpression, Any], right: Union[DoubleExpression, Any]):
        self.left = left
        self.right = right


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
        # ae.left.accept(self)
        self.visit(ae.left)  # system already would know what overloaded visit to use
        self.buffer.append('+')
        # ae.right.accept(self)
        self.visit(ae.right)
        self.buffer.append(')')

    def __str__(self):
        return ''.join(self.buffer)


class ExpressionEvaluator:
    """Stateful visit

    If you have one - sometimes you may need to cache some states"""

    def __init__(self):
        self.value = None  # we will init this value with the value we are visiting

    @dispatch(DoubleExpression)
    def visit(self, de: DoubleExpression):
        self.value = de.value

    @dispatch(AdditionExpression)
    def visit(self, ae: AdditionExpression):
        """ visit left, visit right and add
        BUT when you will visit right side the value will be overridden
        We can fix it with temp value"""
        self.visit(ae.left)  # system already would know what overloaded visit to use
        temp = self.value
        self.visit(ae.right)
        self.value = temp + self.value  # calculate final value


if __name__ == '__main__':
    # 1 + (2 + 3) or
    # 1 + (2 - 3)
    e = AdditionExpression(DoubleExpression(1),
                           AdditionExpression(DoubleExpression(2), DoubleExpression(3))
                           # SubtractionExpression(DoubleExpression(2), DoubleExpression(3))
                           )

    printer = ExpressionPrinter()
    printer.visit(e)
    print(printer)

    evaluator = ExpressionEvaluator()
    evaluator.visit(e)

    print(f"{printer} = {evaluator.value}")
