"""
The common problem with Adapter = too many temporary object
Cause we are regenerating every time a lot of Points to be able to use given API

We will calculate the hash of particular line, and if the hash is same - than reuse that already calculated line
"""
from pprint import pprint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end="")


# ^^ you are given this
# vv

class Line:
    """ Represented as a two Points. """

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


class Rectangle(list):
    """ Represented as a list of lines. """

    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter:
    count = 0  # counter how many calls we are making
    cache = {}

    def __init__(self, line):  # line = line that we want to adapt
        self.h = hash(line)
        if self.h in self.cache:
            return

        self.__class__.count += 1
        print(f'{self.count}: Generating points for line ' +
              f'[{line.start.x},{line.start.y}]→[{line.end.x},{line.end.y}]')

        left = min(line.start.x, line.end.x)
        bottom = min(line.start.y, line.end.y)

        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        # hash the calculated line
        self.cache[self.h] = points  # we can save hash like this ONLY because hash is mutable
        # if we were to save immutable object e.g. int: self.__class__.count

    def __iter__(self):
        """ We are making our object iterable !!! GENIUS !!!"""
        return iter(self.cache[self.h])


def draw(rcs):
    print("\n\n--- Drawing some stuff ---\n")
    for rc in rcs:
        for line in rc:
            """
            The problem is external API is made of points and ours from lines with 2 point in it
            So how should we jump from given API to object that we actually want to use
            Build the adapter
            We need to represent a Line as a series of Points to be able to draw
            Line to Point adapter

            """
            pass
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == '__main__':
    rcs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rcs)
    draw(rcs)  # we are drawing same point one more time so that not super optimized

    print(f"\nTotal lines adapted: {LineToPointAdapter.count}")
    print(f"Total values hashed: {len(LineToPointAdapter.cache)}")
    pprint(LineToPointAdapter.cache)
