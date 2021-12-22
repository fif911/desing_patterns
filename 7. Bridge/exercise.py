# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too
import unittest
from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "lines"


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "pixels"


class Shape:
    def __init__(self, renderer, name):
        self.renderer = renderer
        self.name = name

    def __str__(self):
        return 'Drawing %s as %s' % (self.name, self.renderer.what_to_render_as)
        # return f"Drawing {self.name} as {self.renderer.what_to_render_as}"


class Square(Shape):

    def __init__(self, renderer):
        super().__init__(renderer, name="Square")

    # def __str__(self):
    #     return f"Drawing a {self.name} as {self.renderer.what_to_render_as}"
    # return self.renderer.what_to_render_as
    # return "Drawing Triangle as pixels"


class Triangle(Shape):

    def __init__(self, renderer):
        super().__init__(renderer, name="Triangle")


class Evaluate(unittest.TestCase):
    def test_square_vector(self):
        sq = Square(VectorRenderer())
        self.assertEqual(str(sq), 'Drawing Square as lines')

    def test_pixel_triangle(self):
        tr = Triangle(RasterRenderer())
        self.assertEqual(str(tr), 'Drawing Triangle as pixels')

# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
# str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"
if __name__ == '__main__':
    vector_square = Square(VectorRenderer())
    print(vector_square)
    print(Square(RasterRenderer()))
    print(Triangle(VectorRenderer()))
    print(Triangle(RasterRenderer()))
