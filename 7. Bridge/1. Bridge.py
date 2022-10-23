# drawing application can draw
# circle square
# and can render them in 2 different form
# raster and vector

# VectorCircle VectorSquare RasterCircle RasterSquare
# doing smth like will work BUT
# The problem with this approach doest really scale

# Lets split in different shapes and different renderers
# the question how to make a connection between the shapes and renderers
from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

    @abstractmethod
    def render_square(self, side):
        pass


# S = TypeVar('S', bound=Renderer)  # Can be any subtype of str


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        # implementations for vector circle rendering
        print(f"Drawing a circle of radius {radius}")

    def render_square(self, side):
        print(f"Drawing a square with side = {side}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        # implementations for raster circle rendering
        print(f"Drawing pixels for a circle of radius {radius}")

    def render_square(self, side):
        print(f"Drawing pixels for a square with side = {side}")


# now we need to do hierarchy of shapes
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        # that we are taking renderer as a argument its the core of Bridge design pattern
        # this is how we connect one hierarchy with another
        self.renderer = renderer

    def draw(self): pass

    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius: int):
        super(Circle, self).__init__(renderer)
        self.radius = radius

    def draw(self):
        # here we use the bridge
        # we saved it so rn we can access it to render a circle
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    # circle = Circle(raster, 5)
    circle.draw()
    circle.resize(1.5)
    circle.draw()
