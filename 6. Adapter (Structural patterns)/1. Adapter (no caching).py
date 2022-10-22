"""
imagine we are given some pre packaged API (Point class and draw point func)

Needed to use given API with you custom implementations that are differ from given API
"""
from typing import List


# ===================================== EXTERNAL API
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end="")


# ===================================== END EXTERNAL API


# ^^ you are given this
# vv

class Line:
    """ Represented as two Points. """

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


class Rectangle(list):
    """ Represented as a list of Lines. """

    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter(list):
    """List of Points"""
    count = 0  # class counter how many total conversions we are making

    def __init__(self, line: Line):  # line = line that we want to adapt
        """Receive Line object and convert it the list of Points
        Store result in self
        """
        super().__init__()
        self.__class__.count += 1  # Save value as class variable

        print(f'{self.count}: Generating points for line '
              f'[{line.start.x},{line.start.y}]→'
              f'[{line.end.x},{line.end.y}]')

        # calculate left,right,top,bottom coordinates of the line
        left = min(line.start.x, line.end.x)
        bottom = min(line.start.y, line.end.y)

        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))


def draw(rcs: List[Rectangle]):
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
            adapter: List[Point] = LineToPointAdapter(line)
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
