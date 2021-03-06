#from FreeCAD.src.Mod.Arch.importWebGL import FreeCADGui
# path to your FreeCAD.so or FreeCAD.dll file
# FREECADPATH = 'C:\Program Files\FreeCAD 0.14\lib'
FREECADPATH = 'C:\Program Files\FreeCAD 0.14\lib'
import sys
sys.path.append(FREECADPATH)

import pickle
import FreeCAD


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
        self.shapefunction = []
        self.var = []

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



"""
class PartTestCases(unittest.TestCase):
    def setUp(self):
        self.Doc = FreeCAD.newDocument("PartTest")

    def testBoxCase(self):
        self.Box = App.ActiveDocument.addObject("Part::Box", "Box")
        self.Doc.recompute()
        self.failUnless(len(self.Box.Shape.Faces) == 6)

    def tearDown(self):
        # closing doc
        FreeCAD.closeDocument("PartTest")

    # print ("omit clos document for debuging")
"""

def main():

    doc = FreeCAD.open("C:/Users/User/Desktop/CAD_Data/bridge.FCStd")
    fcverticelist = doc.Sketch.Shape.Vertexes
    fcedgelist = doc.Sketch.Shape.Edges

    edgelist=[]
    numnodes = len(fcverticelist)
    verticelist = []
    for i in range(0, numnodes):
        index = [i,str(id(fcverticelist[i]))]
        coordlist = []
        for j in range(0, 3):
            coordlist.append(fcverticelist[i].Point[j])
        verticelist.append(Vertice(index,coordlist))
    print(verticelist[4].coordinates)

    pickle.dump(verticelist, open("save.p", "wb"))
"""
    for i in range(0, len(edgelist)):
        for j in range(0, 2):
            coordlist=[]
            if
            for k in range(0, 3):
                coordlist.append(edgelist[i].Vertexes[j].Point[k])

            v=Vertice(j,)
        edgelist.append(fcedgelist[])

    pickle.dump(verticelist, open("save.p", "wb" ))

    print(edgelist[3].Vertexes[1].Point[0])
    E1 = len(edgelist)
    print(E1)
    V1 = verticelist[0]
    coord = V1.Point
    coordx = V1.Point[0]
    print(coord)
    print(coordx)
    #can create a geometry in FreeCAD, and read the geometric objects properties.
"""

"""
import Part
b = Part.makeBox(100,100,100)
b.Wires
w = b.Wires[0]
w
w.Wires
w.Vertexes
Part.show(w)
w.Edges
e = w.Edges[0]
e.Vertexes
v = e.Vertexes[0]
v.Point
"""

if __name__ == "__main__":
    main()
