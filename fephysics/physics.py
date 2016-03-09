from femaths.femaths import Femaths
from femaths.femesh import Femesh
from femaths.funreq import Doftype, Meshobjecttype, Funreq
from femaths.funspace import Monomials
from femaths.polytope import Polytopetype, Polygontype, Polyhedrontype, Polygoncoordinate, Polytope
from enum import Enum

class Coordinatesystem(Enum):
    cartesian = 1
    spherical = 2
    cylindric = 3

class Dimension(Enum):
    dim1 = 1
    dim2 = 2
    dim3 = 3

class Geomeabst(Enum):
    point = 0
    line = 1
    surface = 2
    volume = 3

class Acrossvar(Enum):
    voltage = 1
    velocity = 2
    angularvelocity = 3

class Intensive(Enum):
    pressure = 1
    temperature = 2
    electricpotential = 3

class Spaceassociation(Enum):
    volume = 1
    surface = 2
    line = 3
    point = 4
    volumedensity = 5
    surfacedensity = 6
    linedensity = 7
    notdensity = 8

class Timeassociation(Enum):
    intervals = 1
    instantrate = 2
    instantnotrate = 3

class Physicalquantities(Enum):
    constants = 1
    parameters = 2
    variables = 3


class Fegeometry:
    def __init__(self, femaths):
        self.shapefunlist = femaths.shapefunlist

class Fephysics:
    def __init__(self, femaths):
        self.shapefunlist = femaths.shapefunlist

class Modellingspace:
    def __init__(self, feogeometry):
        pass

# vertice are of type physical variables. edges are of type physical equation.
#some vertices are of type derived physical variable
class Mathvartype(Enum):
    scalar = 1
    vector = 2
    axialtensor = 3

class Physicstheory(Enum):
    mechanics = 1
    electrical = 2
    thermal = 3
    magnetic = 4
    fluid = 5

class Physicsvariable:
    def __init__(self, mathvartype, physicstheory, spaceassociation):
        self.mathvartype = mathvartype
        self.physicstheory = physicstheory
        self.spaceassociation = spaceassociation


class Physicsequation:
    def __init__(self, physicsvariable1, physicsvariable2, physicsequationtype):
        try:
            isinstance(physicsvariable1, Physicsvariable)
            isinstance(physicsvariable2, Physicsvariable)
            isinstance(physicsequationtype, Physicsequationtype)
        except:
            raise NameError('entry should be of type Physicsvariable')




class Physicsequationtype(Enum):
    definingequation = 1
    constitutiveequation = 2
    balanceequation = 3

class definingequation(Enum):
    difference = 1
    ratio = 2
    gradient = 3

class Physicsdiagram:
    def __init__(self):
        pass

class Units(Enum):
    meter = 1





def main():

    polytopetype1 = Polytopetype.line
    polygontype1 = Polygontype.nopolygon
    polyhedrontype1 = Polyhedrontype.nopolyhedron
    polytopecoord1 = Polygoncoordinate(polygontype1)
    line = Polytope(polytopetype1, polygontype1, polyhedrontype1, polytopecoord1)
    linemesh = Femesh(line)
    doftype1 = Doftype.pointevaluation
    facedim1 = Meshobjecttype.vertice
    dofnumber1 = 1
    funcreq1 = Funreq(doftype1, facedim1, dofnumber1)
    funreqlist1 = [funcreq1]
    linemesh.applyfunreq(funreqlist1)
    poly1Dlinear_x = Monomials(1, 1, ['x'])
    femathline = Femaths(poly1Dlinear_x,linemesh)
    fegeoline = Fegeometry(femathline)
    fephysics = Fephysics(femathline)
    scalar = Mathvartype.scalar
    vector = Mathvartype.vector
    mechanics = Physicstheory.mechanics
    point = Spaceassociation.point
    thermalconduction = Physicstheory.thermal
    meter = Units.meter
    position = Physicsvariable(vector, mechanics, point, meter)
    displacement = Physicsvariable(vector, mechanics, line, meter)
    differenceequation = definingequation.difference





if __name__ == "__main__":
    main()