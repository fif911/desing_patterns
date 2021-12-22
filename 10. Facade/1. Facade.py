"""
Console consist of
buffer
uport
console class

and console here is a facade
"""
from typing import List


class Buffer:
    """One or two dimensional chunk of memory
    Low level module"""

    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):  # text its list chars
        self.buffer += text


class Viewport:
    """Shows a chunk of the buffer somewhere"""

    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


class Console:
    """Our Facade
    In init we set up the default buffer and default viewport attached to this buffer
    but we also store them so if somebody would want to work with them they would be able to do so
    """

    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport()
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    # we want to expose some methods but also kind of hide the user from the complexity
    # eg if somebody wants to write to the console its obvious that they want to write to currently selected viewport
    # and specifically to the buffer attached to that viewport
    def write(self, text):
        self.current_viewport.buffer.write(text)

    # but if u want to u can expose low level functionality u can access buffers and viewports
    # also we can offer low level api
    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)


if __name__ == '__main__':
    c = Console()
    c.write('text')  # this is what facade is needed for
    ch = c.get_char_at(0)
