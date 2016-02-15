from enum import Enum
from polytope import Polytope, Polytopedimension, Polytopetype
from itertools import combinations
from scipy.special import comb, factorial


class Paramrange(Enum):
    parammin = 0
    parammax = 1


class Femmeshtriangle:
    def __init__(self, polytope):

        if polytope.name == 'line':
            self.edgeconnectivity = list(combinations(range(0, int(polytope.listnumface[0])), 2))
            self.nodecoord = [0, 1]

            verticelist = []
            for i in range(0, int(polytope.listnumface[0])):
                verticelist.append(Vertice([i], self.nodecoord[i]))

            self.verticelist = verticelist

            edgelist = []
            for i in range(0, int(polytope.listnumface[1])):
                edgelist.append(Edge(i,
                                     verticelist[self.edgeconnectivity[i][0]],
                                     verticelist[self.edgeconnectivity[i][1]]))

            self.edgelist = edgelist

        elif polytope.name == 'triangle':
                #self.numberedge = 3
                #self.numbervertice = 3
            self.volumelist = []
            self.facelistindex = [0]
            #self.edgelistindex = [0, 1, 2]
            self.edgeconnectivity = list(combinations(range(0, int(polytope.listnumface[0])),
                                                      int(comb(2, 1))))
            #[[0, 1], [1, 2], [2, 0]]
            #self.nodelistindex = [0, 1, 2]
            self.nodecoord = [[0, 0], [1, 0], [0, 1]]

            verticelist = []
            for i in range(0, int(polytope.listnumface[0])):
                verticelist.append(Vertice([i], self.nodecoord[i]))

            self.verticelist = verticelist

            edgelist = []
            for i in range(0, int(polytope.listnumface[1])):
                edgelist.append(Edge(i,
                                     verticelist[self.edgeconnectivity[i][0]],
                                     verticelist[self.edgeconnectivity[i][1]]))

            self.edgelist = edgelist

        elif polytope.name == 'tetrahedron':
                 #self.numberedge = 3
                #self.numbervertice = 3
            self.volumelist = []
            self.facelistindex = [0]
            #self.edgelistindex = [0, 1, 2]

            self.edgeconnectivity = list(combinations(range(0, int(polytope.listnumface[0])),
                                                      int(comb(2, 1))))
            self.faceconnectivity = list(combinations(range(0, int(polytope.listnumface[1])),
                                                      int(comb(3, 2))))
            #[[0, 1], [1, 2], [2, 0]]
            #self.nodelistindex = [0, 1, 2]
            self.nodecoord = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]

            verticelist = []
            for i in range(0, int(polytope.listnumface[0])):
                verticelist.append(Vertice([i], self.nodecoord[i]))

            self.verticelist = verticelist

            edgelist = []
            for i in range(0, int(polytope.listnumface[1])):
                edgelist.append(Edge(i,
                                     verticelist[self.edgeconnectivity[i][0]],
                                     verticelist[self.edgeconnectivity[i][1]]))

            self.edgelist = edgelist




class Refelements(Enum):
    line = [[1, 2],
            [0, 1]]
    triangle = [[1, 2, 3],
                [[1, 2], [2, 3], [3, 1]],
                [[0, 0], [0, 1], [1, 0]]]
    tetrahedron = [[1, 2, 3, 4],
                   [[3, 5, 1],[3, 4, 2],[2, 6, 1],[4, 6, 5]],
                   [[1, 4], [4, 2], [2, 1], ]
                   ]


class Vertice:
    def __init__(self, index, coordlist):
        try:
            isinstance(coordlist, list)
            isinstance(index, list)
            iterindex = iter(index)
            for i in iterindex:
                i = int(i)
        except:
            raise NameError('index is of list of integers and coordlist is a list')

        self.coordinates = coordlist
        self.index = index

class Edge:
    def __init__(self, index, vertice1, vertice2):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.interiorvertice = []
        self.index = [index]

    def addvertice(self, param):
        if Paramrange.parammin.value <= param <= Paramrange.parammax.value:
            verticecoord = []
            for i in range(0, len(self.vertice1.coordinates)):
                verticecoord.append((self.vertice2.coordinates[i]
                                     - self.vertice1.coordinates[i])*param)
            newindex = [self.index[0], len(self.interiorvertice) + 1]
            addedvertice = Vertice(newindex, verticecoord)
            self.interiorvertice.append(addedvertice)

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

class Femmesh:
    def __init__(self, polytope):
        if isinstance(polytope, Polytope):
            #create vertice of the polytope
            meshelemlist = []
            for i in range(0, len(polytope.polytopedim)+1):
                for k in range(0, len(polytope.listnumface[0])):
                    newvertice = Vertice([k],[u,v,w])
                    meshelemlist.append(newvertice)
                meshelemlist = [meshelemlist]





        else:
            raise NameError('argument should')



def main():
    vertice0 = Vertice([0], [0, 0])
    vertice1 = Vertice([1], [1, 0])
    vertice2 = Vertice([2], [0, 1])
    edge0 = Edge(1, vertice0, vertice1)
    edge1 = Edge(2, vertice1, vertice2)
    edge2 = Edge(3, vertice1, vertice2)
    print(edge1.__dict__)
    edge1.addvertice(.3)
    edge1.addvertice(.6)
    polytopetype0 = Polytopetype.simplex
    polytopedim0 = Polytopedimension.dim1
    polytopetype1 = Polytopetype.simplex
    polytopedim1 = Polytopedimension.dim2
    simplex0 = Polytope(polytopetype0, polytopedim0)
    simplex1 = Polytope(polytopetype1, polytopedim1)
    #fem0 = Femmeshtriangle(simplex0)
    fem1 = Femmeshtriangle(simplex1)
    print(edge1.__dict__)
    print(edge1.interiorvertice[0].__dict__)
    print(edge1.interiorvertice[1].__dict__)
    print(fem1.edgelist.__dict__)


if __name__ == "__main__":
    main()