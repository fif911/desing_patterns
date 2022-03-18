"""
You are asked to write an expression processor for simple numeric expressions with the following constraints:

"""
import timeit
from enum import Enum, auto
from typing import List


class Token:
    class Type(Enum):
        INTEGER = auto()
        VARIABLE = auto()
        PLUS = auto()
        MINUS = auto()

    def __init__(self, type: Type, text: str):
        self.type = type
        self.text = text

    def __str__(self):
        return f'`{self.text}`'


def lex(input) -> List[Token]:
    result = []
    i = 0
    while i < len(input):

        if input[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif input[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif input[i].isdigit():
            digits = [input[i]]

            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1  # increment by 1 so we will not return to this char anymore
                else:
                    break  # if not digit - break and append
            result.append(Token(Token.Type.INTEGER,
                                ''.join(digits)))
        elif input[i].isalpha():
            if i != len(input) - 1 and input[i + 1].isalpha():
                raise ValueError("Variable not single char!")
            result.append(Token(Token.Type.VARIABLE, input[i]))
        else:
            pass
        i += 1

    return result


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value
        else:
            return self.left.value


class Integer:
    def __init__(self, value):
        self.value = value


class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value


def parse(tokens: List[Token], vars: dict):
    # Lets assume than top level result should always be binary expression
    result = BinaryExpression()
    have_lhs = False  # we need it to know whether we need to put it on left hand side or right side of a binary exp
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            # It's just modifier on current expression
            result.type = BinaryExpression.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            # It's just modifier on current expression
            result.type = BinaryExpression.Type.SUBTRACTION
        elif token.type == Token.Type.VARIABLE:
            if token.text in vars:
                integer = Integer(vars[token.text])
                if not have_lhs:
                    result.left = integer
                    have_lhs = True
                else:
                    result.right = integer
            else:
                raise ValueError("variable not set in vars!")
        i += 1
    return result


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression: str):
        """
        1+2 should return 3
        1+ab should return 0
        1+x if x in variables =2 should return 3
        """
        try:
            tokens = lex(expression)
        except ValueError:
            return 0

        try:
            parsed = parse(tokens, self.variables)
        except ValueError:
            return 0

        return parsed.value


if __name__ == '__main__':
    # print(globals())
    # ep = ExpressionProcessor()
    # ep.variables = {'x': 3}
    # print(
    #     ep.calculate("1+2"),
    #     ep.calculate("1+x"),
    #     ep.calculate("1+xa"),
    #     ep.calculate("xa+1"),
    #     ep.calculate("1+a+1"),
    #     sep="\n")
    # ep.variables = {'x': 1, 'a': 2}
    # print(
    #     ep.calculate("x-a"),
    #     sep="\n")

    ep = ExpressionProcessor()
    ep.variables['x'] = 5
    res = timeit.timeit("ep.calculate('1');ep.calculate('1+xa');ep.calculate('1+2');ep.calculate('1+x')",
                        globals=globals(), number=100000)

    print(res)  # 1.5003857
