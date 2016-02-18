# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:00:59 2016

@author: User
"""

from sympy import*
from sympy.polys.monomials import itermonomials
from scipy.special import comb
from sympy.physics.quantum import TensorProduct
from polytope import Polytopetype, Polytopedimension
from funreq import Doftype
from enum import Enum


class Kform(Enum):
    zeroform = 0
    oneform = 1
    twoform = 2
    threeform = 3


class Funspace:
    def __init__(self, polytopetype, polytopedimension, kform, dofnumber):

        try:
            isinstance(polytopetype, Polytopetype)
            isinstance(polytopedimension, Polytopedimension)
            isinstance(kform, Kform)

        except:
            raise NameError('wrong type entry. arg1: Polytopetype, arg2: Polytopedimension, arg3: Kform')

        if polytopedimension.value >= dofnumber:
            raise NameError('Problem cant be represented')

        else:
            listdof = []
            degreemax = 10
            if polytopetype == Polytopetype.simplex:

                for i in range(0, degreemax):
                    listdof.append(comb(polytopedimension.value + i, i))

            elif polytopetype == Polytopetype.cube:

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

                    self.basis = basislist
                    funmat = Matrix(coefvec)*Matrix(basislist)
                    fun = funmat[0]
                    self.fun = fun

            elif self.polytopetype == Polytopetype.cube.name:

                if self.kform == Kform.zeroform.name:

                    for i in range(0, self.dimension):
                        listvar.append(listallvar[i])

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


    def funeval(self, doftype, *args):

        x, y, z = symbols('x y z')
        listallvar =[x, y, z]
        listvar = []

        if isinstance(doftype, Doftype):
            values = []
            for elem in args:
                values.append(elem)

            if len(values) == self.dimension:
                for i in range(0, self.dimension):
                    listvar.append(listallvar[i])

                if doftype == Doftype.pointevaluation:
                    funeval = self.fun
                    for i in range(0, len(values)):
                        funeval = funeval.subs(listvar[i], values[i])

                    return funeval

                if doftype == Doftype.firstderivative:
                    #evaluation can be multidimensional
                    funeval = []
                    #for each variable calculate the first derivative
                    for i in range(0, len(values)):
                        funevalitem = self.fun
                        funevalitem = diff(funevalitem, listvar[i], 1)
                        #for each first derivative calculate the derivative value
                        for k in range(0, len(values)):
                            funevalitem = funevalitem.subs(listvar[k], values[k])
                        funeval.append(funevalitem)

                    return funeval

            else:
                raise NameError('number of arguments is of same dimension as polytope')

        else:
            raise NameError('entry doftype has to be of type doftype')




def main():
    polytopetype1 = Polytopetype.simplex
    dimension1 = Polytopedimension.dim2
    kform1 = Kform.zeroform
    dofnumber1 = 10
    doftype1 = Doftype.pointevaluation
    doftype2 = Doftype.firstderivative
    funspace1 = Funspace(polytopetype1, dimension1, kform1, dofnumber1)
    print(funspace1.__dict__)
    polyeval1 = funspace1.funeval(doftype1,1,1)
    print(polyeval1)
    polyeval2 = funspace1.funeval(doftype2,1,1)
    print(polyeval2)
#
#    dimension2 = 1
#    polytopetype2 = 'cube'
#    dofnumber2 = 6
#    kform2 = 0
#    funspace2 = Funspace(dimension2, dofnumber2, polytopetype2, kform2)
#    poly2 = funspace2.getfun()
#    print(poly2)


if __name__ == "__main__":
    main()
