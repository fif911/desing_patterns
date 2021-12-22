"""
From drawing application we know that we can drag&drop shapes individually but also we can group several shapes
and drag&drop hem together as if they were a single shape

So what we made here
we made sure that the GraphicObject gets to pretend as being either scalar base class for something like
Square or Circle indeed a collection by keeping a set of children and then printing those children whenever
somebody asks you for
"""


class GraphicObject:
    """
    this class can be either serve as a base class for a single shape like circle or
    to hold a group of object together

    duo use functionality
    """

    def __init__(self, color=None):
        self.color = color
        self.children = []
        self._name = "Group"

    @property
    def name(self):
        # why we using _name to expose the name through the property
        # just to show that you can override this in the inheritance
        return self._name

    def _print(self, items, depth):
        """
        utility method to draw nice
        recursive function

        It defines what we need to print. Cause essentially(по сути) we dont know of we have any items
        if we have items - we need to print every single one of them starting with the *
        otherwise we just print ourselves
        (that's due use functionality right inside this utility method)
        """
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        """output of drawing in console"""
        items = []  # set of items that we want to collate (объединять) (a set of strings that we want to print)
        self._print(items, 0)  # get all the items at a particular level of depth
        # this is why we have this pseudo internal method, cause we want to provide a depth and this is a
        # recursive operation
        return ''.join(items)


# graphic object by itself its just a container for other objects
# but we can also inherit from it to have concrete classes

class Circle(GraphicObject):

    @property
    def name(self):
        # override the name getter
        return "Circle"


class Square(GraphicObject):

    @property
    def name(self):
        # override the name getter
        return "Square"


# rn we can construct a grouping of objects as well as individual objects
# and we also can have groupings of groupings

if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = "My drawing"  # it's bad to do so. Just fo illustration purposes
    # that we can give a GraphicObject different name

    drawing.children.append((Square('Red')))
    drawing.children.append((Circle('Yellow')))

    # we also can have a group and and this group to the drawing
    group = GraphicObject() # no name
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))
    drawing.children.append(group)

    print(drawing)
    """
    My drawing      # is a group
    *RedSquare
    *YellowCircle
    *Group          # that contains group
    **BlueCircle
    **BlueSquare
    """

