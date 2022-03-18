"""
Turn tokens into expression tree that you can traverse using typically a Visitor patter to order either print the expression
or evaluate

First of all we need to parse and receive some tree
"""

from enum import Enum, auto
from typing import List, Union


class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LPAREN = 3
        RPAREN = 4

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
        elif input[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif input[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:  # must be a number
            digits = [input[i]]

            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1  # increment by 1 so we will not return to this char anymore
                else:
                    break  # if not digit - break and append
            result.append(Token(Token.Type.INTEGER,
                                ''.join(digits)))
        i += 1

    return result


class Integer:
    def __init__(self, value):
        self.value = value


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
        else:
            return self.left.value - self.right.value


def parse(tokens: List[Token]):
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
        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                # find right parentheses to make a subexp, parse it recursively
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)  # recursive call
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        i += 1
    return result


def calc(input):
    tokens = lex(input)  # get tokens. Its lexing process
    print(' '.join(map(str, tokens)))

    parsed = parse(tokens)
    print(f'{input} = {parsed.value}')


if __name__ == '__main__':
    calc('(13+4)-(12+1)')
    calc('1+(3-4)')

    # this won't work
    calc('1+2+(3-4)')