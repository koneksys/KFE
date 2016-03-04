# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:00:59 2016

@author: User
"""

from sympy import*
from funreq import Funreq, Fieldtype, Doftype, Meshobjecttype
from scipy.special import comb
from sympy.physics.quantum import TensorProduct

#from polytope import Polytopetype, Polytopedimension
#from funreq import Doftype
from enum import Enum



def funeval(funspace, doftype, coord):
    try:
        isinstance(doftype, Doftype)
        isinstance(coord, list)
        len(coord) == len(funspace.basis)
    except:
        raise NameError('first argument is of type DOF and second of type coord')

    if doftype == Doftype.pointevaluation:
        funeval = funspace.fun
        for i in range(0, len(coord)):
            funeval = funeval.subs(funspace.var[i], coord[i])

        return funeval

    elif doftype == Doftype.firstderivative:
        #evaluation can be multidimensional
        funeval = []
        #for each variable calculate the first derivative
        for i in range(0, len(coord)):
            funevalitem = funspace.fun
            funevalitem = diff(funevalitem, funspace.var[i], 1)
            #for each first derivative calculate the derivative value
            for k in range(0, len(coord)):
                funevalitem = funevalitem.subs(funspace.var[k], coord[k])
            funeval.append(funevalitem)

        return funeval


class Monomial:
    def __init__(self, dimension, degree, varnamelist):

        try:
            isinstance(varnamelist, list)
            isinstance(dimension, int)
            isinstance(degree, int)
            len(varnamelist) == degree
            for var in varnamelist:
                isinstance(var, str)
            0 < dimension <= 3
            0 < degree
        except:
            raise NameError('dimension and degree of type integer with 0<dimension<=3, 0<degree, '
                            'list with element of type string and length varname == degree')
        varsymbollist=[]
        for var in varnamelist:
            varsymbollist.append(symbols(var))


        #calculate the number of degree of freedom
        self.dofnumber = int(comb(dimension+degree, degree))

        coefvec = MatrixSymbol('c', 1, self.dofnumber)

        monomiallist = [1]
        if dimension == 1:
            for i in range(1, degree+1):
                for k in range(0, dimension):
                    monomiallist.append(pow(varsymbollist[0], i))

        elif dimension == 2:
            for i in range(1, degree+1):
                monomiallist.append(pow(varsymbollist[0], i))
                for j in range(1, i):
                    monomiallist.append(pow(varsymbollist[0], i-j)*pow(varsymbollist[1], j))
                monomiallist.append(pow(varsymbollist[1], i))

        elif dimension == 3:
            for i in range(1, degree+1):
                monomiallist.append(pow(varsymbollist[0], i))
                for j in range(1, i):
                    monomiallist.append(pow(varsymbollist[0], i-j)*pow(varsymbollist[1], j))
                monomiallist.append(pow(varsymbollist[1], i))

                for j in range(1, i):
                    monomiallist.append(pow(varsymbollist[0], i-j)*pow(varsymbollist[2], j))

                for j in range(1, i):
                    monomiallist.append(pow(varsymbollist[1], i-j)*pow(varsymbollist[2], j))
                monomiallist.append(pow(varsymbollist[2], i))

        self.basis = monomiallist
        self.var = varsymbollist
        funmat = Matrix(coefvec)*Matrix(monomiallist)
        fun = funmat[0]
        self.fun = fun

    def funeval(self, doftype, *args):
        return funeval(self, doftype, *args)


class Tensorspace:
    def __init__(self, *args):
        monolist = []
        try:
            for elem in args:
                isinstance(elem, Monomial)
                monolist.append(elem)
        except:
            raise NameError('arguments are of type Monomial')

        if len(monolist) > 3:
            raise NameError('not more than three dimension')
        #actually test should be more elaborate. one could 2 dimension * 1 dimension thus only having 2 arguments


        self.monolist = monolist

        dofnumber = 1
        for i in range(0,len(monolist)):
            dofnumber = dofnumber * len(monolist[i].basis)

        self.dofnumber = dofnumber

        coefvec = MatrixSymbol('c', 1, dofnumber)

        if len(monolist) == 1:
            self.basis = monolist[0].basis
            self.fun = monolist[0].fun

        elif len(monolist) == 2:
            basismat = TensorProduct(Matrix(monolist[0].basis), Matrix(monolist[1].basis))
            funmat = Matrix(coefvec)*Matrix(basismat)
            fun = funmat[0]
            self.fun = fun

        elif len(monolist) == 3:
            basismat = TensorProduct(Matrix(monolist[0].basis), Matrix(monolist[1].basis))
            basismat = TensorProduct(basismat, Matrix(monolist[2].basis))
            funmat = Matrix(coefvec)*Matrix(basismat)
            fun = funmat[0]
            self.fun = fun

        basis=[]
        for i in basismat:
            basis.append(i)
        self.basis = basis

    def funeval(self, doftype, *args):
        return funeval(self, doftype, *args)



def main():
#    polytopetype1 = Polytopetype.simplex
#    dimension1 = Polytopedimension.dim2
#    dofnumber1 = 10
#    doftype1 = Doftype.pointevaluation
#    doftype2 = Doftype.firstderivative
#    funspace1 = Funspace(polytopetype1, dimension1, dofnumber1)
#    print(funspace1.__dict__)
#    polyeval1 = funspace1.funeval(doftype1,1,1)
#    print(polyeval1)
#    polyeval2 = funspace1.funeval(doftype2,1,1)
#    print(polyeval2)
    poly1Dlinear_x = Monomial(2, 2, ['x','y'])
    poly1Dlinear_y = Monomial(1, 1, ['y'])
    poly1Dlinear_z = Monomial(1, 1, ['z'])
    PE = Doftype.pointevaluation
    FD = Doftype.firstderivative
    a=poly1Dlinear_x.funeval(FD, [1,1])
    print(a)
    print(poly1Dlinear_x.__dict__)
    tensorpoly = Tensorspace(poly1Dlinear_x,poly1Dlinear_y,poly1Dlinear_z)
    print(tensorpoly.__dict__)
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
