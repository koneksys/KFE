from femaths.femath import Femath
from femaths.femesh import Femesh
from femaths.funreq import Doftype, Meshobjecttype, Funreq
from femaths.funspace import Monomials
from femaths.polytope import Polytopetype, Polygontype, Polyhedrontype, Polygoncoordinate, Polytope
from enum import Enum
from sympy import*

class Coordinatesystem(Enum):
    cartesian = 1
    spherical = 2
    cylindric = 3

class Units(Enum):
    meter = 1
    newton = 2
    sqmeter = 3
    newtonsqmeter = 4
    density = 5
    dimensionless = 6

class Mathvartype(Enum):
    scalar = 1
    vector = 2
    tensor = 3

class Physicstheory(Enum):
    mechanics = 1
    electrical = 2
    thermal = 3
    magnetic = 4
    fluid = 5
    none = 6

class Physicsvartype(Enum):
    configuration = 1
    source = 2
    energy = 3
    power = 4
    geometry = 5
    material = 6

class Modellspacedim(Enum):
    dim1 = 1
    dim2 = 2
    dim3 = 3

class Geometryvar(Enum):
    point = 0
    line = 1
    surface = 2
    volume = 3

class Physicsvar:
    def __init__(self, mathvartype, units, varsymbol, physicstheory, physicsvartype, Physicsvarlist):
        self.symbol = varsymbol
        self.mathvartype = mathvartype
        self.units = units
        self.physicstheory = physicstheory
        self.Physicsvarlist = Physicsvarlist




class Fevar:
    def __init__(self, femaths, physicsvar, modellingdim):
        self.shapefunlist = femaths.shapefunlist
        if physicsvar.mathvartype == Mathvartype.vector:
            vect = MatrixSymbol(physicsvar.symbol, 1, modellingdim)
        elif physicsvar.mathvartype == Mathvartype.scalar:



class Fegeom:
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
    femathline = Femath(poly1Dlinear_x, linemesh)
    print(femathline.__dict__)
    vector = Mathvartype.vector
    scalar = Mathvartype.scalar
    mechanics = Physicstheory.mechanics
    none = Physicstheory.none
    coordsystemtype = Coordinatesystem.cartesian
    configvar = Physicsvartype.configuration
    sourcevar = Physicsvartype.source
    geometryvar = Physicsvartype.geometry
    materialvar = Physicsvar.material
    meter = Units.meter
    sqmeter = Units.sqmeter
    newton = Units.newton
    nounit = Units.dimensionless
    forcedensity = Units.density
    nwtsqmeter = Units.newtonsqmeter
    surface = Geometryvar.surface
    force = Physicsvar(vector,newton,'F',mechanics,sourcevar,[])
    surface = Physicsvar(vector,sqmeter,'A', none,geometryvar,[])
    stress = Physicsvar(tensor,nwtsqmeter,'s',mechanics,sourcevar,[force,surface])
    directionofchange = Physicsvar(vector,meter,'doc',configvar,mechanics,[])
    referenceline = Physicsvar(vector,meter,'rf',configvar,mechanics,[])
    strain = Physicsvar(tensor,nounit,'ep',[directionofchange,referenceline])
    bodyload = Physicsvar(scalar,forcedensity,'f',sourcevar,[])
    Elasticity = Physicsvar(tensor,nounit,'E',)
    elasticityvar = [force, surface, stress, directionofchange, referenceline, strain, bodyload]
    forcebar = force.setdim(1)
    surfacebar = surface.setdim(1)
    stressbar = stress.setdim(1)
    dirofchangebar = directionofchange.setdim(1)
    referenceline = referenceofline.setdim('nochange')
    strainbar =

    force1D = force.setdim(1) = point
    surface1D = surface.setdim(1) = point
    stress = stress.setdim(1) = point


    forcetype = (vector, point)
    stresstype = (scalar, point)
    straintype = (scalar, line)
    displacementtype = (vector, point)
    displacement = Physicsvar(vector,meter,'u')
    #displacementint = Fevar(femathline, displacement, modellingdim)
    #linemodelspace = Fegeom(femathline, coordsystemtype, modellingdim)
    #inputmodel = [force, displacement]
    #barelem = femodel(Fephyvar,Fegeometry,inputmodel,outputmodel)







if __name__ == "__main__":
    main()