from __future__ import annotations


class Point:
    name = None

    def __init__(self, x=0, y=0, name=None):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        if self.name is not None:
            return "{}({},{})".format(self.name, self.x, self.y)
        else:
            return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise Exception("Both parameters have to be of type Point!")
        return abs(self.x - other.x) <= 1e-05 and abs(self.y - other.y) <= 1e-05

    def __hash__(self):
        return hash(("%.3f" % (self.x), "%.3f" % (self.y)))
