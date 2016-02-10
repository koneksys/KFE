# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:00:59 2016

@author: User
"""

from sympy import*
from sympy.polys.monomials import itermonomials
from scipy.special import comb
from sympy.physics.quantum import TensorProduct
from femaths.polytope import Polytopetype, Polytopedimension
from femaths.funreq import Doftype
from enum import Enum


class Kform(Enum):
    zeroform = 0
    oneform = 1
    twoform = 2
    threeform = 3


class Funspace:
    def __init__(self, polytopetype, polytopedimension, kform, dofnumber):

        test1 = isinstance(polytopetype, Polytopetype)
        test2 = isinstance(polytopedimension, Polytopedimension)
        test3 = isinstance(kform, Kform)

        if test1 and test2 and test3:

            if polytopedimension.value >= dofnumber:
                raise NameError('Problem cant be represented')

            else:
                listdof = []
                degreemax = 10
                if polytopetype.name == Polytopetype.simplex.name:

                    for i in range(0, degreemax):
                        listdof.append(comb(polytopedimension.value + i, i))

                elif polytopetype.name == Polytopetype.cube.name:

                    for i in range(0, degreemax):
                        listdof.append(pow(i+1, polytopedimension.value))

                else:
                    raise NameError('polytopetype is not supported')

                if dofnumber in listdof:
                    self.degree = listdof.index(dofnumber)
                    self.dimension = polytopedimension.value
                    self.polytopetype = polytopetype.name
                    self.dofnumber = int(dofnumber)
                    self.kform = kform.name
                    self.basis = None
                    self.fun = None

                else:
                    raise NameError('Problem cant be represented')

                x,y,z = symbols('x y z')
                listallvar =[x,y,z]
                listvar = []
                basisset = {}
                basislist = []
                coefvec = MatrixSymbol('c', 1, self.dofnumber)
                funmat = []

                if self.polytopetype == Polytopetype.simplex.name:

                    if self.kform == Kform.zeroform.name:

                        for i in range(0, self.dimension):
                            listvar.append(listallvar[i])

                        basisset = itermonomials(listvar, self.degree)

                        for elem in basisset:
                            basislist.append(elem)

                        funmat = Matrix(coefvec)*Matrix(basislist)
                        fun = funmat[0]
                        self.fun = fun

                elif self.polytopetype == Polytopetype.cube.name:

                    if self.kform == Kform.zeroform.name:

                        for i in range(0, self.dimension):
                            listvar.append(listallvar[i])

                        b = []
                        for i in range(0, self.dimension):
                            basisset = itermonomials([listvar[i]], self.degree)
                            basislist = []
                            for elem in basisset:
                                basislist.append(elem)

                            self.basis = basislist

                            if i == 0:
                                basis = Matrix(basislist)
                            if i == 1:
                                basis = TensorProduct(basis, Matrix(basislist))
                            if i == 2:
                                basis = TensorProduct(basis, Matrix(basislist))

                        funmat = Matrix(coefvec)*Matrix(basis)
                        fun = funmat[0]

                        self.fun = fun

        else:
            raise NameError('wrong type entry. arg1: Polytopetype, arg2: Polytopedimension, arg3: Kform')


#    def getfun(self, doftype):
#        if isinstance(doftype, Doftype):
#            if doftype.name == Doftype.pointevaluation:






def main():
    polytopetype1 = Polytopetype.simplex
    dimension1 = Polytopedimension.dim2
    kform1 = Kform.zeroform
    dofnumber1 = 3
    funspace1 = Funspace(polytopetype1, dimension1, kform1, dofnumber1)
    print(funspace1.__dict__)
#    dimension2 = 1
#    polytopetype2 = 'cube'
#    dofnumber2 = 6
#    kform2 = 0
#    funspace2 = Funspace(dimension2, dofnumber2, polytopetype2, kform2)
#    poly2 = funspace2.getfun()
#    print(poly2)


if __name__ == "__main__":
    main()
