# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:29:48 2016

@author: User
"""

from scipy.special import comb, factorial
from enum import Enum


class Polygontype(Enum):
    nopolygon = 2
    triangle = 3
    square = 4
    pentagon = 5
    hexagon = 6
    octogon = 8


class Polytopecoordinate(Enum):
    zstart = [0, 0, 1]
    line = [0, 1]
    triangle = [[0, 0], [0, 1], [1, 1]]
    square = [[0, 0], [0, 1], [1, 1], [0, 1]]


class Polytopetype(Enum):
    line = 1
    polygon = 2
    polyhedron = 3


class Polyhedrontype(Enum):
    nopolyhedron = 0
    pyramid = 1
    prism = 2


class Polytope:
    def __init__(self, polytopetype, polygontype, polyhedrontype):
        try:
            isinstance(polytopetype, Polytopetype)
            isinstance(polygontype, Polygontype)
            isinstance(polyhedrontype, Polyhedrontype)
        except:
            raise NameError('first argument is Polytopetype: line, polygon, polyhedron'
                            'second argument is polygontype: nopolygon, triangle, square, pentagon..'
                            'third argument is polyhedrontype: nopolyhedron, pyramid, prism ')

        self.polytopename = [polytopetype.name, polygontype.name, polyhedrontype.name]
        self.listnumface = []
        self.verticelist = []
        self.edgelist = []
        self.facelist = []

        if polytopetype.value == 1:
            self.listnumface = [1, 2]

        if polytopetype.value == 2:
            self.listnumface = [1, polygontype.value, polygontype.value]

        if polytopetype.value == 3 and polyhedrontype.value == 1:
            self.listnumface = [1, polygontype.value + 1,
                                2 * polygontype.value, polygontype.value + 1]

        if polytopetype.value == 3 and polyhedrontype.value == 2:
            self.listnumface = [1, 2 + polygontype.value,
                                3 * polygontype.value, 2 * polygontype.value  ]


def main():
    polytopetype1 = Polytopetype.line
    polygontype1 = Polygontype.nopolygon
    polyhedrontype1 = Polyhedrontype.nopolyhedron
    LineElement = Polytope(polytopetype1, polygontype1, polyhedrontype1)
    polytopetype2 = Polytopetype.polygon
    polygontype2 = Polygontype.triangle
    polyhedrontype2 = Polyhedrontype.nopolyhedron
    triangleElement = Polytope(polytopetype2, polygontype2, polyhedrontype2)
    polytopetype3 = Polytopetype.polyhedron
    polygontype3 = Polygontype.square
    polyhedrontype3 = Polyhedrontype.pyramid
    triangularprism = Polytope(polytopetype3, polygontype3, polyhedrontype3)

    print(LineElement.__dict__)
    print(triangleElement.__dict__)
    print(triangularprism.__dict__)



if __name__ == "__main__":
    main()
