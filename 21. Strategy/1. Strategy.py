"""
Text processor to process different elements and output them into either HTML or Markdown
"""
from abc import ABC
from enum import Enum, auto
from typing import Type


class ListStrategy(ABC):
    """Interface to which every list strategy should conform to
    (Blueprint of the algorithm)
    Note interface does not have implementations itself"""

    def start(self, buffer):
        """Append the start of the list to the buffer"""
        pass

    def end(self, buffer):
        """Append the start of the list to the buffer"""
        pass

    def add_list_item(self, buffer, item):
        """The key one, where we add item to the buffer"""
        pass


class MarkdownListStrategy(ListStrategy):
    """MarkDown List Strategy

    Does not require some specific start and end"""

    def add_list_item(self, buffer, item):
        buffer.append(f" * {item}\n")


class HTMLListStrategy(ListStrategy):
    """HTML List Strategy

    Has opening and closing tags"""

    def start(self, buffer):
        buffer.append("<ul>\n")

    def end(self, buffer):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer, item):
        buffer.append(f"    <li>{item}</li>\n")


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class TextProcessor:
    def __init__(self, list_strategy: ListStrategy = HTMLListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        ls = self.list_strategy

        ls.start(self.buffer)
        for i in items:
            ls.add_list_item(self.buffer, i)
        ls.end(self.buffer)

    def set_output_format(self, format_to_output):
        if format_to_output == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format_to_output == OutputFormat.HTML:
            self.list_strategy = HTMLListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)


if __name__ == '__main__':
    items = ["foo", "bar", "baz"]

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)

    # Change the strategy in the runtime
    tp.set_output_format(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)
