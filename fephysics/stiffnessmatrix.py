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


class Fegeo:
    def __init__(self, femaths, dimension, coordinatesystem):
        self.mesh = femaths.mesh
        self.dimension = dimension
        self.shapefunlist = femaths.shapefunlist
        self.coordinatesystem = coordinatesystem
        self.coord = Matrix(MatrixSymbol('x', dimension, dimension))



class Fevar:
    def __init__(self, femaths):
        if len(femaths.listnumface) == 2:
            self.mesh = femaths.mesh
            self.dofnumber = femaths.dofnumber
            self.listnumface = femaths.listnumface
            self.shapefunlist = femaths.shapefunlist
            self.paramvar = femaths.var[0]
            u = Matrix(MatrixSymbol('u', 1, self.dofnumber))
            self.mesh[0].vertice1.var = u[self.mesh[0].vertice1.index[0]]
            self.mesh[0].vertice2.var = u[self.mesh[0].vertice2.index[0]]

            stiffnessmatrix = zeros(self.dofnumber, self.dofnumber)
            gradientshapefunlist = []

            for i in range(0, self.dofnumber):
                gradientshapefunlist.insert(i, diff(femaths.shapefunlist[i][1], femaths.var[0], 1))
                gradientshapevector = Matrix(gradientshapefunlist)
                gradientshapematrix = gradientshapevector*gradientshapevector.transpose()
            for i in range(0, self.dofnumber):
                for j in range(0, self.dofnumber):
                    p = Poly(gradientshapematrix[i, j], femaths.var[0])
                    pi = p.integrate(femaths.var[0])
                    stiffnessmatrix[i,j] = pi(femaths.mesh[0].vertice2.coordinates[0])\
                              - pi(femaths.mesh[0].vertice1.coordinates[0])

            self.stiffnessmatrix = stiffnessmatrix

    def settomodelspace(self, dimension, fegeo):
            #we have already the coordinate as vectors - now we have to adjust the number of DOF in phyvar.
            u = Matrix(MatrixSymbol('u', dimension, self.dofnumber)).transpose()
            self.u = u
            tangentspace = []
            for i in range(0,len(fegeo.shapefunlist)):
                tangentspace.append(diff(fegeo.shapefunlist[i][1], self.paramvar, 1))

            shapefunvector=[]
            for i in range(0,len(self.shapefunlist)):
                shapefunvector.append(self.shapefunlist[i][1])

            tangentspace = (Matrix(tangentspace)).transpose()*(fegeo.coord)
            displacement = Matrix(shapefunvector).transpose()*u
            self.tangentspace = tangentspace
            self.tangentdisplacement = tangentspace*displacement.transpose()
            #implement tangentdisplacement
            self.parametricstrain = diff(self.tangentdisplacement[0], self.paramvar, 1)
            strainmodelspace = []

            for i in range(0,dimension):
                strainmodelspace.append((1/
                                         (self.tangentspace[i])
                                         * self.parametricstrain))

            self.strainmodelspace = strainmodelspace

            #self.mesh[0].vertice1.var = u[self.mesh[0].vertice1.index[0]]
            #self.mesh[0].vertice2.var = u[self.mesh[0].vertice2.index[0]]


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
    fevar = Fevar(femathline)
    fegeo = Fegeo(femathline, 2,'cartesian')
    fevar.settomodelspace(2, fegeo)
    a = 2
"""    print(femathline.__dict__)
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
    directionofchange = Physicsvar(vector,meter,'doc',mechanics, configvar,mechanics,[])
    referenceline = Physicsvar(vector,meter,'rf',mechanics, configvar,[])
    strain = Physicsvar(tensor,nounit,'ep',mechanics, configvar, [directionofchange,referenceline])
    bodyload = Physicsvar(scalar,forcedensity,'f',mechanics, sourcevar,[])
    Elasticityconstant = Physicsvar(tensor,nounit,'E',mechanics, configvar, [stress, surface])

    elasticityvar = [force, surface, stress, directionofchange, referenceline, strain, bodyload, Elasticityconstant]
    forcebar = force.setdim(1)
    surfacebar = surface.setdim(1)
    stressbar = stress.setdim(1)
    directionofchangebar = directionofchange.setdim(1)
    referenceline = referenceline.setdim('nochange')
    strainbar = strain.setdim(1)
    bodyload = bodyload.setdim(1)
    Elasticityconstantbar = Elasticityconstant.setdim(1)




    forcetype = (vector, point)
    stresstype = (scalar, point)
    straintype = (scalar, line)
    displacementtype = (vector, point)
    displacement = Physicsvar(vector,meter,'u')
    #displacementint = Fevar(femathline, displacement, modellingdim)
    #linemodelspace = Fegeom(femathline, coordsystemtype, modellingdim)
    #inputmodel = [force, displacement]
    #barelem = femodel(Fephyvar,Fegeometry,inputmodel,outputmodel)


"""




if __name__ == "__main__":
    main()