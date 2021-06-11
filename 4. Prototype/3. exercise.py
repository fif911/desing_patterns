import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        # new_start_p = Point(self.start.x,self.start.y)
        # new_end_p = Point(self.end.x,self.end.y)
        # return Line(new_start_p,new_end_p)
        return copy.deepcopy(self)
