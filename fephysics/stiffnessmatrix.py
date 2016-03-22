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
        self.dofnumber = femaths.dofnumber
        self.shapefunlist = femaths.shapefunlist
        self.coordinatesystem = coordinatesystem
        self.coordvar = ['x','y','z']
        coordvarmatrix = zeros(dimension,self.dofnumber)
        for i in range(0,dimension):
            for j in range(0, self.dofnumber):
                coordvarmatrix[i,j] = symbols(self.coordvar[i]+str(j))
        self.coord = coordvarmatrix


class Fevar:
    def __init__(self, femaths, physicsvar):
        if len(femaths.listnumface) == 2:
            self.mesh = femaths.mesh
            self.dofnumber = femaths.dofnumber
            self.listnumface = femaths.listnumface
            self.shapefunlist = femaths.shapefunlist
            self.phyvarsymbol = physicsvar.symbol
            self.mathvartype = physicsvar.mathvartype
            self.paramvar = femaths.var[0]

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

    def settomodelspace(self, fegeo):

        dimension = fegeo.dimension
        #define the freevariable representing the degrees of freedom of the physical system in the modelling space
        phyvarmatrix = zeros(dimension,self.dofnumber)
        for i in range(0,dimension):
            for j in range(0, self.dofnumber):
                phyvarmatrix[i,j] = symbols(self.phyvarsymbol+str(j)+fegeo.coordvar[i])
        self.phyvarmatrix = phyvarmatrix

        #define the vector of shapefunctions to represent the physical value - the scalar product
        shapefunvec = []
        for i in range(0,self.dofnumber):
                shapefunvec.append(self.shapefunlist[i][1])

        # of phyvarmatrix and this vector gives the expression of the physical variable
        self.phymodfun = phyvarmatrix * Matrix(shapefunvec)


        if self.mathvartype == Mathvartype.vector:
            #we have to calculate the tangent vector...
            tangentvector = zeros(dimension, 1)
            Norm = 0
            for i in range(0, dimension):
                    tangentvector[i] = 0
                    for j in range(0, self.dofnumber):
                        tangentvector[i] = tangentvector[i] + \
                                               diff(fegeo.shapefunlist[j][1], self.paramvar, 1) * fegeo.coord[i,j]

                    Norm = Norm + tangentvector[i] * tangentvector[i]
            self.Norm = sqrt(Norm)


            self.unittangentvector = (1/self.Norm)*eye(dimension) * tangentvector

            self.tangentphyvarunit = self.phymodfun.transpose() * self.unittangentvector
            self.tangentphyvar = self.phymodfun.transpose() * self.unittangentvector
            #self.phymodfun.transpose() * tangentvector

        elif self.mathvartype == Mathvartype.scalar:
            self.tangentphyvar = self.phymodfun

        self.gradientvar = diff(self.tangentphyvar[0], self.paramvar, 1)*(1/Norm)
        self.gradientvar = expand(self.gradientvar)

        tuplephyvar = []
        for i in range(0, dimension):
            for j in range(0,self.dofnumber):
                tuplephyvar.append(phyvarmatrix[i,j])
        tuplephyvar = tuple(tuplephyvar)

        self.collectexp = collect(self.gradientvar, tuplephyvar,evaluate=false)
        gradientvector = zeros(1, self.dofnumber*dimension)
        index = 0


        for i in range(0, self.dofnumber):
            for j in range(0, dimension):
                gradientvector[index] = self.collectexp[phyvarmatrix[j,i]]
                index = index + 1

        self.gradientvector = Matrix(gradientvector)

        modelstiffnessmatrix = zeros(self.dofnumber*dimension, self.dofnumber*dimension)
        self.gradientshapematrix = self.gradientvector.transpose()*self.gradientvector
        for i in range(0, self.dofnumber*dimension):
            for j in range(0, self.dofnumber*dimension):
                p = Poly(self.gradientshapematrix[i, j], self.paramvar)*self.Norm
                pi = p.integrate(self.paramvar)
                I = (pi(self.mesh[0].vertice2.coordinates[0])\
                          - pi(self.mesh[0].vertice1.coordinates[0]))
                modelstiffnessmatrix[i,j] = simplify(I)

        self.modelstiffnessmatrix = modelstiffnessmatrix

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
    doftype2 = Doftype.pointevaluation
    facedim2 = Meshobjecttype.edge
    dofnumber2 = 1
    funcreq2 = Funreq(doftype2, facedim2, dofnumber2)

    funreqlist2 = [funcreq1]
    linemesh.applyfunreq(funreqlist2)
    poly1Dlinear_x = Monomials(1, 1, ['s'])

    vector = Mathvartype.vector
    scalar = Mathvartype.scalar

    mechanics = Physicstheory.mechanics
    none = Physicstheory.none
    coordsystem = Coordinatesystem.cartesian
    configvar = Physicsvartype.configuration
    sourcevar = Physicsvartype.source
    geometryvar = Physicsvartype.geometry
    materialvar = Physicsvartype.material

    meter = Units.meter
    sqmeter = Units.sqmeter
    newton = Units.newton
    nounit = Units.dimensionless
    forcedensity = Units.density
    nwtsqmeter = Units.newtonsqmeter
    surface = Geometryvar.surface

    displacement = Physicsvar(vector, meter, 'u', mechanics, configvar, [])
    force = Physicsvar(vector, newton, 'F', mechanics, sourcevar, [])
    surface = Physicsvar(vector, sqmeter, 'A', none, geometryvar, [])
    stress = Physicsvar(tensor, nwtsqmeter, 's', mechanics, sourcevar, [force,surface])
    directionofchange = Physicsvar(vector, meter, 'doc', mechanics, configvar, [])
    referenceline = Physicsvar(vector, meter, 'rf', mechanics, configvar, [])
    strain = Physicsvar(tensor, nounit, 'ep', mechanics, configvar, [directionofchange,referenceline])
    bodyload = Physicsvar(scalar, forcedensity, 'f', mechanics, sourcevar, [])
    Elasticityconstant = Physicsvar(tensor, nounit, 'E', mechanics, configvar, [stress, surface])

    femathline = Femath(poly1Dlinear_x, linemesh)
    fevar = Fevar(femathline, displacement)
    fegeo3D = Fegeo(femathline, 3, coordsystem)
    fegeo2D = Fegeo(femathline, 2, coordsystem)
    fegeo1D = Fegeo(femathline, 1, coordsystem)
    fevar.settomodelspace(fegeo1D)

    elasticityvar = [force, surface, stress, directionofchange, referenceline, strain, bodyload, Elasticityconstant]
    a=2

if __name__ == "__main__":
    main()