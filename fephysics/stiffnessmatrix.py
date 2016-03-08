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

class Mathvartype(Enum):
    scalar = 1
    vector = 2
    axialtensor = 3

class Modellspacedim(Enum):
    dim1 = 1
    dim2 = 2
    dim3 = 3

class Spaceassociation(Enum):
    point = 0
    line = 1
    surface = 2
    volume = 3

class Fephyvar:
    def __init__(self, femaths, physicsvartype, modellingdim):
        self.shapefunlist = femaths.shapefunlist
class Fegeometry:
    def __init__(self, femaths):
        self.shapefunlist = femaths.shapefunlist


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
    vector = Mathvartype.vector
    scalar = Mathvartype.scalar
    modellingdim = Modellspacedim.dim2
    coordsystemtype = Coordinatesystem.cartesian
    point = Spaceassociation.point
    line = Spaceassociation.line
    force = (vector, point)
    stress = (scalar, point)
    strain = (scalar, line)
    displacement = (vector, point)
    displacementint = Fephyvar(femathline, displacement, modellingdim)
    linemodelspace = Fegeometry(femathline, coordsystemtype, modellingdim)
    inputmodel = [force, displacement]
    barelem = femodel(Fephyvar,Fegeometry,inputmodel,outputmodel)







if __name__ == "__main__":
    main()