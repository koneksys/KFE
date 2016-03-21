#from FreeCAD.src.Mod.Arch.importWebGL import FreeCADGui
# path to your FreeCAD.so or FreeCAD.dll file
# FREECADPATH = 'C:\Program Files\FreeCAD 0.14\lib'
FREECADPATH = 'C:\Program Files\FreeCAD 0.14\lib'
import sys
sys.path.append(FREECADPATH)
from femaths.femesh import Vertice,Edge

import FreeCAD


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
    verticelist = doc.Sketch.Shape.Vertexes
    edgelist = doc.Sketch.Shape.Edges

    for i in range(0, len(edgelist)):


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
"""""

if __name__ == "__main__":
    main()
