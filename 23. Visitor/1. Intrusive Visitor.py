"""Simple numeric expression that we want to take in object-oriented format and work with them (print & evaluate)

There is no classic visitor, but we can think of a buffer object that is visiting

We see intrusive solution that goes against OCP
"""
from typing import List, Union, Any


class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer: List):
        """Print everything into a buffer"""
        buffer.append(str(self.value))

    def eval(self):
        return self.value


class AdditionExpression:
    def __init__(self, left: Union[DoubleExpression, Any], right: Union[DoubleExpression, Any]):
        self.left = left
        self.right = right

    def print(self, buffer: List):
        """Print everything into a buffer"""
        buffer.append('(')
        self.left.print(buffer)  # NIIICCEE. We call the DoubleExpression stored, and it automatically append to buffer
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()


if __name__ == '__main__':
    # 1 + (2 + 3)
    e = AdditionExpression(DoubleExpression(1),
                           AdditionExpression(DoubleExpression(2), DoubleExpression(3))
                           )

    """Now to allow Double Expression and Addition Expression to be printable
    In intrusive approach we do not make visitor as such. 
    
    We modify our source classes to allow them to be printable
    Which, obviously, does not scale and breaks OCP
    """

    buffer = []
    e.print(buffer)

    print(''.join(buffer))

    """
    If we want to add another behaviour like eval() we need to change our hierarchy of classes once more
    """

    print(''.join(buffer) + " = " + str(e.eval()))
