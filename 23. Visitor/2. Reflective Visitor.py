"""
Improving the Intrusive approach with
Separate class for printing (we extracted printing concerns (as SRP tolds us to do))

This approach  reflective approach as in some programming languages checking of the type is a reflection operation

There is a downside of this implementation: we need to modify ExpressionPrinter everytime we add new inheritors
"""
from __future__ import annotations

import inspect
from abc import ABC
from typing import List, Union, Any
import logging

logger = logging.Logger(__name__)


class Expression(ABC):
    """Class to what we will dynamically add functionality"""
    pass


class DoubleExpression(Expression):  # add inheritance
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):  # add inheritance
    def __init__(self, left: Union[DoubleExpression, Any], right: Union[DoubleExpression, Any]):
        self.left = left
        self.right = right


class ExpressionPrinter:
    """Visitor

    All printing logic is kept in a separate class and we do not modify DoubleExpression and AdditionExpression
    This class has static method for Expression Printer"""

    @staticmethod
    def print_printer(expression: AdditionExpression | DoubleExpression, buffer: List):
        # we don't know what type of expression we received, so we need to do type checking

        # TODO: (downside) If we add new inheritor (e.g. SubtractionExpression), it will be ignored and not printed
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print_printer(expression.left,
                                            buffer)  # NIIIICE reuse method we are currently in recursively:
            buffer.append('+')
            ExpressionPrinter.print_printer(expression.right, buffer)
            buffer.append(')')

    # lambda function that take expression and lambda and adds the functionality in class definition time
    logger.error(f"Expression . print not there yet {dir(Expression)}")
    logger.error(f".print in Expression: {'print' in dir(Expression)}")

    # TODO: WOW. 'lambda expression, buffer: ... ' expression IS SELF by FACT. that's why we can call
    # e.print(buffer) -> and pass only buffer. As self would be passed automatically
    Expression.print = lambda expression, buffer: ExpressionPrinter.print_printer(expression, buffer)
    logger.error(f"Expression . print added {dir(Expression)}")
    logger.error(f".print in Expression: {'print' in dir(Expression)}")
    print(Expression.print)
    print(inspect.getfullargspec(Expression.print))


if __name__ == '__main__':
    # 1 + (2 + 3)
    e = AdditionExpression(DoubleExpression(1),
                           AdditionExpression(DoubleExpression(2), DoubleExpression(3))
                           )

    buffer = []

    # e will be passed as self
    e.print(buffer)  # IDE will complain as print method is added in runtime

    # Also will work:
    buffer.append('\n')
    # but here we need to pass e and buffer
    ExpressionPrinter.print_printer(e, buffer)  # Call Visitor

    print(''.join(buffer))
