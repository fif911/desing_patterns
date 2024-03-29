from enum import Enum


class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LPAREN = 3
        RPAREN = 4

    def __init__(self, type: Type, text):
        self.type: Token.Type = type
        self.text: str = text

    def __str__(self):
        return f'`{self.text}`'


def lex(input):
    result = []
    i = 0
    while i < len(input):  # Needed as it will allow to control incrementor (not possible with for loop + enumerate() )

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


def calc(input):
    tokens = lex(input)  # get tokens. Its lexings process
    print(' '.join(map(str, tokens)))

    # parsed = parse(tokens)
    # print(f'{input} = {parsed.value}')


if __name__ == '__main__':
    calc('(13+4)-(12+1)-(1132)-100')
