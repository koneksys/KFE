# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:29:48 2016

@author: User
"""

from scipy.special import comb, factorial
from enum import Enum
import copy


class Polygontype(Enum):
    nopolygon = 2
    triangle = 3
    square = 4
    pentagon = 5
    hexagon = 6
    octogon = 8


class Polygoncoordinate:
    def __init__(self, polygontype):

        try:
            isinstance(polygontype, Polygontype)
        except:
            raise NameError('argument should be of type Polygontype')

        self.zbase = [0, 0, 0]
        self.ztop = [0, 0, 1]
        self.value = []

        if polygontype == Polygontype.nopolygon:
            self.value = [[0], [1]]

        elif polygontype == Polygontype.triangle:
            self.value = [[0, 0], [1, 0], [0, 1]]

        elif polygontype == Polygontype.square:
            self.value = [[0, 0], [1, 0], [1, 1], [0, 1]]

        elif polygontype == Polygontype.pentagon:
            self.value = [[0.5, 0], [1.5, 0], [2, 1], [1, 2], [0, 1]]


class Polytopetype(Enum):
    line = 1
    polygon = 2
    polyhedron = 3


class Polyhedrontype(Enum):
    nopolyhedron = 0
    pyramid = 1
    prism = 2


class Polytope:
    def __init__(self, polytopetype, polygontype, polyhedrontype, polygoncoordinate):
        try:
            isinstance(polytopetype, Polytopetype)
            isinstance(polygontype, Polygontype)
            isinstance(polyhedrontype, Polyhedrontype)
            isinstance(polygoncoordinate, Polygoncoordinate)

        except:
            raise NameError('first argument is Polytopetype: line, polygon, polyhedron'
                            'second argument is polygontype: nopolygon, triangle, square, pentagon..'
                            'third argument is polyhedrontype: nopolyhedron, pyramid, prism ')

        self.polytopename = [polytopetype.name, polygontype.name, polyhedrontype.name]
        self.polytopeinfo = [polytopetype, polygontype, polyhedrontype]
        self.listnumface = []
        self.verticelist = []
        self.edgelist = [[], []]
        self.facelist = [[], []]

        if polytopetype == Polytopetype.line:
            self.listnumface = [2, 1]
            self.verticelist = [[1, 2], polygoncoordinate.value]

        if polytopetype == Polytopetype.polygon:
            self.listnumface = [polygontype.value, polygontype.value, 1]
            self.verticelist = [range(0, polygontype.value), polygoncoordinate.value]

            for i in range(0, polygontype.value):
                self.edgelist[1].append([i%len(self.verticelist[0]), (i+1)%len(self.verticelist[0])])
            self.edgelist[0] = range(0, polygontype.value)


        if polytopetype == Polytopetype.polyhedron and polyhedrontype == Polyhedrontype.pyramid:
            self.listnumface = [polygontype.value + 1, 2 * polygontype.value, polygontype.value + 1, 1]

            #Generate the verticelist - make a copy in the zcoord plane
            for i in range(0, polygontype.value):
                polygoncoordinate.value[i].append(0)
            polygoncoordinate.value.append(polygoncoordinate.ztop)
            self.verticelist = [range(0, polygontype.value + 1), polygoncoordinate.value]

            #list listnumface[2] should be changed to listnumface[1]
            #listnumface[1] should be changed to listnumface[2]
            #Generate the Edgelist:
            baseindex = range(0, polygontype.value)
            for i in range(0, polygontype.value):
                self.edgelist[1].append([(i)%len(baseindex), (i+1)%len(baseindex)])
                self.edgelist[1].append([i, polygontype.value])
            self.edgelist[0].append(range(0, self.listnumface[1]))

            #Generate the Facelist:
            cycleindex = range(0, self.listnumface[1])
            for i in range(0, self.listnumface[2]-1):
                self.facelist[1].append([(2*i)%len(cycleindex), (2*i+3)%len(cycleindex), -1*((2*i+1)%len(cycleindex))])
                self.facelist[0].append(i)
            #adding the face of the basis:
            self.facelist[0].append(self.listnumface[2])
            self.facelist[1].append(range(0,self.listnumface[1], 2))


        if polytopetype == Polytopetype.polyhedron and polyhedrontype == Polyhedrontype.prism:
            self.listnumface = [1, 2 + polygontype.value,
                                3 * polygontype.value, 2 * polygontype.value]

           #Generate the verticelist - make a copy in the zcoord plane
            coord = copy.deepcopy(polygoncoordinate.value)
            coord.extend(copy.deepcopy(polygoncoordinate.value))

            for i in range(0, polygontype.value):
                coord[i].append(0)
                coord[i+polygontype.value].append(1)

            self.verticelist = [range(0, 2*polygontype.value), coord]

            for i in range(0, polygontype.value):
                self.edgelist[1].append([i%len(self.verticelist[0]), (i+1)%len(self.verticelist[0])])
            self.edgelist[0] = range(0, polygontype.value)
            copyedgelist = copy.deepcopy(self.edgelist[1])

            for i in range(0,2):
                for k in range(0,2):
                    copyedgelist[i][k] = copyedgelist[i][k]+ polygontype.value
            self.edgelist[1].extend(copyedgelist)



def main():
    polytopetype1 = Polytopetype.line
    polygontype1 = Polygontype.nopolygon
    polyhedrontype1 = Polyhedrontype.nopolyhedron
    polytopecoord1 = Polygoncoordinate(polygontype1)
    line = Polytope(polytopetype1, polygontype1, polyhedrontype1,polytopecoord1)

    polytopetype2 = Polytopetype.polygon
    polygontype2 = Polygontype.triangle
    polyhedrontype2 = Polyhedrontype.nopolyhedron
    polytopecoord2 = Polygoncoordinate(polygontype2)
    triangle = Polytope(polytopetype2, polygontype2, polyhedrontype2, polytopecoord2)

    polytopetype3 = Polytopetype.polyhedron
    polygontype3 = Polygontype.triangle
    polytopecoord3 = Polygoncoordinate(polygontype3)
    polyhedrontype3 = Polyhedrontype.pyramid
    triangularpyramid = Polytope(polytopetype3, polygontype3, polyhedrontype3, polytopecoord3)

    polygontype4 = Polygontype.triangle
    polytopetype4 = Polytopetype.polyhedron
    polyhedrontype4 = Polyhedrontype.prism
    polytopecoord4 = Polygoncoordinate(polygontype4)
    triangularprism = Polytope(polytopetype4, polygontype4, polyhedrontype4, polytopecoord4)

#    print(line.__dict__)
    print(triangle.__dict__)
    print(triangularpyramid.__dict__)
#    print(pentagonalpyramid.__dict__)
#    print(triangularprism.__dict__)




if __name__ == "__main__":
    main()
