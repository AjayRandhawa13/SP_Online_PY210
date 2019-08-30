#!/usr/bin/env python3

class Circle(object):
    _radius = None
    _diameter = None

    def __init__(self, radius):
        try:
            self._radius = float(radius)
            self._diameter = float(radius) * 2
        except ValueError:
            raise TypeError("radius expects a float")


    @property
    def radius(self):
        return self._radius


    @property
    def diameter(self):
        return self._diameter
