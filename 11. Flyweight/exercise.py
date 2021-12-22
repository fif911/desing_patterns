class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split(" ")
        self.formatting = []

    class TextRange:
        """Flyweight"""

        def __init__(self, word_pos, capitalize=False):
            self.word_pos = word_pos
            self.capitalize = capitalize

        def covers(self, position):
            """whether char position is the formatted area of text"""
            return position == self.word_pos

    def __getitem__(self, item) -> TextRange:
        _range = self.TextRange(item)
        self.formatting.append(_range)
        return _range

    def __str__(self):
        result = []
        # for i in range(len(self.plain_text)):
        for i, w in enumerate(self.words):
            for tr in self.formatting:
                if tr.covers(i):
                    if tr.capitalize:
                        w = w.upper()

            result.append(w)
        return " ".join(result)


if __name__ == '__main__':
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    sentence[1].capitalize = True
    print(sentence)
