from enum import Enum
from polytope import Polygontype, Polytopecoordinate, Polytopetype, Polyhedrontype, Polytope
from itertools import combinations
from scipy.special import comb, factorial
from funreq import Funreq, Doftype, Meshobjecttype

class Paramrange(Enum):
    parammin = 0
    parammax = 1


class Vertice:
    def __init__(self, index, coordlist):
        try:
            isinstance(coordlist, list)
            isinstance(index, list)

        except:
            raise NameError('index is of list of integers and coordlist is a list')

        self.coordinates = coordlist
        self.index = index
        self.funreq = []

class Edge:
    def __init__(self, index, vertice1, vertice2):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.interiorvertices = []
        self.index = [index]


    def addvertice(self, param):
        if Paramrange.parammin.value <= param <= Paramrange.parammax.value:
            verticecoord = []
            for i in range(0, len(self.vertice1.coordinates)):
                verticecoord.append((self.vertice2.coordinates[i]
                                     - self.vertice1.coordinates[i])*param)
            newindex = [self.index[0], len(self.interiorvertices) + 1]
            addedvertice = Vertice(newindex, verticecoord)
            self.interiorvertices.append(addedvertice)

        else:
            raise NameError('param should be comprised in range defined by Class Paramrange')


class Face:
    def __init__(self, index, edgelist):
        test = True
        iteredgelist = iter(edgelist)
        for i in iteredgelist:
            test = test and isinstance(i, Edge)

        if test is True:
            self.edgelist = edgelist
            self.index = [index]

        else:
            raise NameError('element in list are not of type class Edge')

    def addvertice(self, paramlist):
        test = True
        iterparamlist = iter(paramlist)
        for i in paramlist:
            test = test and (i >= Paramrange.parammin.value) and (i <= Paramrange.parammax.value)

        if test is True:
            verticecoord = []
            vertice = edgelist[0].vertice1.coordinates
            return vertice

        else:
            raise NameError('param should be comprised in range defined by Class Paramrange')


class Femesh:
    def __init__(self, polytope):
        try:
            isinstance(polytope, Polytope)
        except:
            raise NameError('the entry is an object of class Polytope')

        verticelist = []
        edgelist = []

        if polytope.polytopeinfo[0] == Polytopetype.line:
            nbvertice = len(polytope.verticelist[0])
            for i in range(0, nbvertice):
                verticelist.append(Vertice([i], polytope.verticelist[1][i]))

            self.edgelist = Edge(1, verticelist[0], verticelist[1])
            self.verticelist = verticelist

        if polytope.polytopeinfo[0] == Polytopetype.polygon:
            nbvertice = len(polytope.verticelist[0])
            for i in range(0, nbvertice):
                verticelist.append(Vertice([i], polytope.verticelist[1][i]))

            self.verticelist = verticelist

    def applyfunreq(self, reqlist):
        try:
            isinstance(reqlist, list)
            for i in reqlist:
                isinstance(i,Funreq)
        except:
            raise NameError('Argument is of type list with elements of type Funreq')

        for i in range(0, len(reqlist)):
            if reqlist[i].info[1] == Meshobjecttype.vertice:
                for k in range (0, len(self.verticelist)):
                    self.verticelist[k].funreq.append(reqlist[i].info[0])


def main():
    polytopetype1 = Polytopetype.line
    polygontype1 = Polygontype.nopolygon
    polyhedrontype1 = Polyhedrontype.nopolyhedron
    polytopecoord1 = Polytopecoordinate(polygontype1)
    line = Polytope(polytopetype1, polygontype1, polyhedrontype1,polytopecoord1)
    linemesh = Femesh(line)

    polytopetype2 = Polytopetype.polygon
    polygontype2 = Polygontype.triangle
    polyhedrontype2 = Polyhedrontype.nopolyhedron
    polytopecoord2 = Polytopecoordinate(polygontype2)
    triangle = Polytope(polytopetype2, polygontype2, polyhedrontype2, polytopecoord2)
    trianglemesh = Femesh(triangle)

    doftype1 = Doftype.pointevaluation
    facedim1 = Meshobjecttype.vertice
    dofnumber1 = 1
    funcreq1 = Funreq(doftype1, facedim1, dofnumber1)
    doftype1 = Doftype.firstderivative
    facedim1 = Meshobjecttype.vertice
    dofnumber1 = 1
    funcreq2 = Funreq(doftype1, facedim1, dofnumber1)
    funreqlist1 = [funcreq1, funcreq2]
    linemesh.applyfunreq(funreqlist1)
    trianglemesh.applyfunreq(funreqlist1)

    vertice0 = Vertice([0], [0, 0])
    vertice1 = Vertice([1], [1, 0, 0])
    vertice2 = Vertice([2], [0, 1, 1])
    edge0 = Edge(1, vertice0, vertice1)
    edge1 = Edge(2, vertice1, vertice2)
    edge2 = Edge(3, vertice1, vertice2)
    print(edge1.__dict__)
    edge1.addvertice(.3)
    edge1.addvertice(.6)
    print(edge1.__dict__)
    print(edge1.interiorvertices[0].__dict__)
    print(edge1.interiorvertices[1].__dict__)
    print(linemesh.__dict__)




if __name__ == "__main__":
    main()