from enum import Enum
from polytope import Polygontype, Polygoncoordinate, Polytopetype, Polyhedrontype, Polytope
from itertools import combinations
from scipy.special import comb, factorial
from funreq import Funreq, Doftype, Meshobjecttype
from sympy import Rational

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
        try:
            isinstance(vertice1, Vertice)
            isinstance(vertice2, Vertice)
            isinstance(vertice1.coordinates, list)
            isinstance(vertice2.coordinates, list)

        except:
            raise NameError('index is of list of integers')

        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.interiorvertices = []
        self.index = [index]

    def addvertice(self, param):
        try:
            0 <= param <= 1

        except:
            raise NameError('param should be comprised between 0 and 1')
        #use linear shape function to calculate the coordinate of the interior vertice
        if isinstance(self.vertice1.coordinates, int):
            dimension = 1
        else:
            dimension = len(self.vertice1.coordinates)
        newcoord = []
        for i in range(0, dimension):
            newcoord.append(Rational((1-param)*float(self.vertice1.coordinates[i]) +
                            param * float(self.vertice2.coordinates[i])))
        newindex = [self.index[0], len(self.interiorvertices) + 1]
        addedvertice = Vertice(newindex, newcoord)
        self.interiorvertices.append(addedvertice)



class Face:
    def __init__(self, index, edgelist):

        try:
            iteredgelist = iter(edgelist)
            for i in iteredgelist:
                isinstance(i, Edge)
            isinstance(index,list)

            self.edgelist = edgelist
            self.index = [index]

        except:
            raise NameError('first element is a list of indexes, second argument is a list of element of type'
                            'edge')

    def addvertice(self, paramlist):

        try:
            isinstance(paramlist, list)
            len(paramlist) == 2

        except:
            raise NameError('argument is of type list with len(list) == 2')


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
        self.listnumface = polytope.listnumface

        if polytope.polytopeinfo[0] == Polytopetype.line:
            nbvertice = len(polytope.verticelist[0])
            for i in range(0, nbvertice):
                verticelist.append(Vertice([i], polytope.verticelist[1][i]))

            self.edgelist = [Edge(1, verticelist[0], verticelist[1])]
            self.verticelist = verticelist
            self.dimension = 1

        if polytope.polytopeinfo[0] == Polytopetype.polygon:
            nbvertice = len(polytope.verticelist[0])
            nbedge = len(polytope.edgelist[0])
            for i in range(0, nbvertice):
                verticelist.append(Vertice([i], polytope.verticelist[1][i]))

            self.verticelist = verticelist

            for i in range(0, nbedge):
                edgelist.append(Edge(polytope.edgelist[0][i],
                                          self.verticelist[polytope.edgelist[1][i][0]],
                                                           self.verticelist[polytope.edgelist[1][i][1]]))
            self.edgelist = edgelist
            self.dimension = 2

    def applyfunreq(self, reqlist):
        try:
            isinstance(reqlist, list)
            for i in reqlist:
                isinstance(i, Funreq)
        except:
            raise NameError('Argument is of type list with elements of type Funreq')


        self.reqlist = reqlist
        #All requirements applied to an edge should have the same number of DOF.
        ndofedgelist = []
        for i in range(0, len(reqlist)):
            if reqlist[i].info[1] == Meshobjecttype.edge:
                ndofedgelist.append(reqlist[i].dofnumber)

        if len(ndofedgelist)>=1:
            iterator = iter(ndofedgelist)
            first = next(iterator)
            try:
                all(first == rest for rest in iterator)
            except:
                raise NameError('All requirement types applied to an edge should have DOFnumber.')

        #We need to separate the adding of the nodes from the adding of the requirements-
        #first we add the node if there are at least on requirement on the edges.
        if len(ndofedgelist) > 0:
            nbdofonedge = ndofedgelist[0]
            nbedge = len(self.edgelist)
            param = [x*pow(nbdofonedge+1,-1) for x in range(1, nbdofonedge+1)]
            for i in range(0, nbedge):
                for k in range(0, nbdofonedge):
                    self.edgelist[i].addvertice(param[k])

        for i in range(0, len(reqlist)):
            if reqlist[i].info[1] == Meshobjecttype.vertice:
                for k in range(0, len(self.verticelist)):
                    self.verticelist[k].funreq.append(reqlist[i].info[0])

            if reqlist[i].info[1] == Meshobjecttype.edge:
                for k in range(0, len(self.edgelist)):
                    for j in range(0, nbdofonedge):
                        self.edgelist[k].interiorvertices[j].funreq.append(reqlist[i].info[0])

        #calculate the number of DOF:
        nbdof = 0
        for i in range(0, len(reqlist)):
            if reqlist[i].info[0] == Doftype.pointevaluation:
                if reqlist[i].info[1]== Meshobjecttype.vertice:
                    nbdof = nbdof + self.listnumface[0]
                elif reqlist[i].info[1]== Meshobjecttype.edge:
                    nbdof = nbdof + self.listnumface[1]*reqlist[i].dofnumber
                elif reqlist[i].info[1] == Meshobjecttype.face:
                    nbdof = nbdof + self.listnumface[2]*reqlist[i].dofnumber
            if reqlist[i].info[0] == Doftype.firstderivative:
                if reqlist[i].info[1]== Meshobjecttype.vertice:
                    nbdof= nbdof + self.listnumface[0]*(len(self.listnumface)-1)
                elif reqlist[i].info[1]== Meshobjecttype.edge:
                    nbdof = nbdof + self.listnumface[1]*reqlist[i].dofnumber*(len(self.listnumface)-1)
                elif reqlist[i].info[1] == Meshobjecttype.face:
                    nbdof = nbdof + self.listnumface[2]*reqlist[i].dofnumber*(len(self.listnumface)-1)

        self.dofnumber = nbdof




def main():
    polytopetype1 = Polytopetype.line
    polygontype1 = Polygontype.nopolygon
    polyhedrontype1 = Polyhedrontype.nopolyhedron
    polytopecoord1 = Polygoncoordinate(polygontype1)
    line = Polytope(polytopetype1, polygontype1, polyhedrontype1,polytopecoord1)
    linemesh = Femesh(line)

    polytopetype2 = Polytopetype.polygon
    polygontype2 = Polygontype.triangle
    polyhedrontype2 = Polyhedrontype.nopolyhedron
    polytopecoord2 = Polygoncoordinate(polygontype2)
    triangle = Polytope(polytopetype2, polygontype2, polyhedrontype2, polytopecoord2)
    trianglemesh = Femesh(triangle)

    polytopetype3 = Polytopetype.polygon
    polygontype3 = Polygontype.square
    polyhedrontype3 = Polyhedrontype.nopolyhedron
    polytopecoord3 = Polygoncoordinate(polygontype3)
    square = Polytope(polytopetype3, polygontype3, polyhedrontype3, polytopecoord3)
    squaremesh = Femesh(square)

    doftype1 = Doftype.pointevaluation
    facedim1 = Meshobjecttype.vertice
    dofnumber1 = 1
    funcreq1 = Funreq(doftype1, facedim1, dofnumber1)

    doftype2 = Doftype.firstderivative
    facedim2 = Meshobjecttype.vertice
    dofnumber2 = 1
    funcreq2 = Funreq(doftype2, facedim2, dofnumber2)

    doftype3 = Doftype.pointevaluation
    facedim3 = Meshobjecttype.edge
    dofnumber3 = 3
    funcreq3 = Funreq(doftype3, facedim3, dofnumber3)

    doftype4 = Doftype.firstderivative
    facedim4 = Meshobjecttype.edge
    dofnumber4 = 3
    funcreq4 = Funreq(doftype4, facedim4, dofnumber4)
    funreqlist1 = [funcreq1,funcreq2,funcreq3,funcreq4]
    linemesh.applyfunreq(funreqlist1)
    trianglemesh.applyfunreq(funreqlist1)
    squaremesh.applyfunreq(funreqlist1)


    vertice0 = Vertice([0], [0, 0])
    vertice1 = Vertice([1], [1,0])
    vertice2 = Vertice([2], [0,1])
    edge0 = Edge(1, vertice0, vertice1)
    edge1 = Edge(2, vertice1, vertice2)
    edge2 = Edge(3, vertice1, vertice2)
    print(edge1.__dict__)
    edge1.addvertice(.3)
    edge1.addvertice(.6)
    print(edge1.__dict__)
    print(edge1.interiorvertices[0].__dict__)
    print(edge1.interiorvertices[1].__dict__)
    print(trianglemesh.__dict__)




if __name__ == "__main__":
    main()