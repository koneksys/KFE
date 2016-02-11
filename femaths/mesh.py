from enum import Enum


class Paramrange(Enum):
    parammin = -1
    parammax = 1

class Vertice:
    def __init__(self, index, *args):
        coordinates = []
        for elem in args:
            coordinates.append(elem)
        self.coordinates = coordinates
        self.index = [index]

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
        self.edgelist = edgelist

        self.coordinates = coordinates
        self.index = [index]


def main():
    vertice0 = Vertice(0, 0, 0)
    vertice1 = Vertice(1, 1, 0)
    vertice2 = Vertice(2, 0, 1)
    edge0 = Edge(1, vertice0, vertice1)
    edge1 = Edge(2, vertice1, vertice2)
    edge2 = Edge(3, vertice1, vertice2)
    print(edge1.__dict__)
    edge1.addvertice(.3)
    edge1.addvertice(.6)
    print(edge1.__dict__)
    print(edge1.interiorvertice[0].__dict__)
    print(edge1.interiorvertice[1].__dict__)


if __name__ == "__main__":
    main()