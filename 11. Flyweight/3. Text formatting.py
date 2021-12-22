"""

"""


class FormattedText:
    def __init__(self, plain_text: str):
        self.plain_text = plain_text.lower()
        self.caps = [False] * len(plain_text)  # arrays to store index of capitalized char

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            result.append(c.upper() if self.caps[i] else c)
        return ''.join(result)


class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        """Flyweight"""

        def __init__(self, start: int, end: int, capitalize=False, bold=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize
            self.bold = bold

        def covers(self, position):
            """whether char position is the formatted area of text"""
            return self.start <= position <= self.end

    def get_range(self, start, end) -> TextRange:
        _range = self.TextRange(start, end)
        self.formatting.append(_range)
        return _range

    def __str__(self):
        result = []
        # for i in range(len(self.plain_text)):
        for i, c in enumerate(self.plain_text):
            # c = self.plain_text[i]  # get the letter
            for tr in self.formatting:
                if tr.covers(i):
                    if tr.capitalize:
                        c = c.upper()
                    if tr.bold:
                        c = f"*{c}*"

            result.append(c)
        return "".join(result)


if __name__ == '__main__':
    text = "This is a brave new world"
    ft = FormattedText(text)
    ft.capitalize(10, 15)
    ft.capitalize(0, 1)
    print(ft)
    """
    And this works fine. But if u image that in text variable war and peace is loaded up
    We would be allocating (выделить) are too many Boolean values (cause in caps we have arrays of size of plain text)
    
    If the size of text is massive we would be allocating too much data that we mostly fo not need
    e.g. we want to allocate 1 word in 1 million words
    
    lets do smth different
    """
    bft = BetterFormattedText(text)
    bft.get_range(10, 15).capitalize = True
    bft.get_range(0, 0).bold = True
    bft.get_range(0, 0).capitalize = True

    print(bft)
