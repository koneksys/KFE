# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:00:59 2016

@author: User
"""

from sympy import*
from sympy.polys.monomials import itermonomials
from scipy.special import comb
from sympy.physics.quantum import TensorProduct


class Funspace:
    def __init__(self, dimension, dofnumber, polytopetype, kform):

        if dimension >= dofnumber:
            raise NameError('Problem cant be represented')

        else:
            listdof = []
            degreemax = 6
            if polytopetype == 'simplex':

                for i in range(0,degreemax):
                    listdof.append(comb(dimension + i, i))

            elif polytopetype == 'cube':

                for i in range(0,degreemax):
                    listdof.append(pow(i+1,dimension))

            else:
                raise NameError('Problem cant be represented')

            if dofnumber in listdof:
                self.degree = listdof.index(dofnumber)
                self.dimension = dimension
                self.polytopetype = polytopetype
                self.dofnumber = dofnumber
                self.kform = kform
                self.basis = None
                self.fun = None

            else:
                raise NameError('Problem cant be represented')

    def getfun(self):

        if self.polytopetype == 'simplex':
            return funsimplex(self.dimension, self.kform, self.degree, self.dofnumber)

        elif self.polytopetype == 'cube':
            return funcube(self.dimension, self.kform, self.degree, self.dofnumber)


def funsimplex(dimension, kform, degree, dofnumber):
    x,y,z = symbols('x y z')
    listallvar =[x,y,z]
    listvar = []
    basisset = {}
    basislist = []
    coefvec = MatrixSymbol('c', 1, dofnumber)
    funmat = []

    if kform == 0:

        for i in range(0,dimension):
            listvar.append(listallvar[i])

        basisset = itermonomials(listvar, degree)

        for elem in basisset:
            basislist.append(elem)

        funmat = Matrix(coefvec)*Matrix(basislist)
        fun = funmat[0]

        return fun


def funcube(dimension, kform, degree, dofnumber):
    x,y,z = symbols('x y z')
    listallvar = [x, y, z]
    listvar = []
    basisset = {}
    basislist = []
    coefvec = MatrixSymbol('c', 1, dofnumber)
    funmat = []

    if kform == 0:

        for i in range(0,dimension):
            listvar.append(listallvar[i])

        b = []
        for i in range(0, dimension):
            basisset = itermonomials([listvar[i]], degree)
            basislist = []
            for elem in basisset:
                basislist.append(elem)

            if i == 0:
                basis = Matrix(basislist)
            if i == 1:
                basis = TensorProduct(basis, Matrix(basislist))
            if i == 2:
                basis = TensorProduct(basis, Matrix(basislist))

        funmat = Matrix(coefvec)*Matrix(basis)
        fun = funmat[0]

        return fun



def main():

    dimension1 = 2
    polytopetype1 = 'simplex'
    dofnumber1 = 6
    kform1 = 0
    funspace1 = Funspace(dimension1, dofnumber1, polytopetype1, kform1)
    poly1 = funspace1.getfun()
    print(poly1)

    dimension2 = 2
    polytopetype2 = 'cube'
    dofnumber2 = 9
    kform2 = 0
    funspace2 = Funspace(dimension2, dofnumber2, polytopetype2, kform2)
    poly2 = funspace2.getfun()
    print(poly2)


if __name__ == "__main__":
    main()
