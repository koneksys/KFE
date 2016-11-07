"""
 KFE
 * http://www.koneksys.com/
 *
 * Copyright 2016 Koneksys
 * Released under the MIT license
 *
 * @author Jerome Szarazi (jerome.szarazi@koneksys.com)
 */
"""



import unittest

from scipy.special import comb

from femath.polytope import Polytope, Polytopedimension, Polytopetype
from femath.funspace import Funspace, Kform


class FunspaceTest(unittest.TestCase):
    def test_simplexline(self):
        polytopetype = Polytopetype.simplex
        polytopedim = Polytopedimension.dim1
        kform = Kform.zeroform
        listdofnumbertest = calcdof(polytopetype, polytopedim, degreemaxtest=5)
        print(listdofnumbertest)
        for i in range(0, len(listdofnumbertest)):
            dofnumber = listdofnumbertest[i]
            funspace = Funspace(polytopetype, polytopedim, kform, dofnumber)
            print(funspace.__dict__)

    def test_simplextriangle(self):
        polytopetype = Polytopetype.simplex
        polytopedim = Polytopedimension.dim2
        kform = Kform.zeroform
        listdofnumbertest = calcdof(polytopetype, polytopedim, degreemaxtest=5)
        print(listdofnumbertest)
        for i in range(0, len(listdofnumbertest)):
            dofnumber = listdofnumbertest[i]
            funspace = Funspace(polytopetype, polytopedim, kform, dofnumber)
            print(funspace.__dict__)

    def test_simplextetrahedron(self):
        polytopetype = Polytopetype.simplex
        polytopedim = Polytopedimension.dim3
        kform = Kform.zeroform
        listdofnumbertest = calcdof(polytopetype, polytopedim, degreemaxtest=5)
        print(listdofnumbertest)
        for i in range(0, len(listdofnumbertest)):
            dofnumber = listdofnumbertest[i]
            funspace = Funspace(polytopetype, polytopedim, kform, dofnumber)
            print(funspace.__dict__)

    def test_cubeline(self):
        polytopetype = Polytopetype.cube
        polytopedim = Polytopedimension.dim1
        kform = Kform.zeroform
        listdofnumbertest = calcdof(polytopetype, polytopedim, degreemaxtest=5)
        print(listdofnumbertest)
        for i in range(0, len(listdofnumbertest)):
            dofnumber = listdofnumbertest[i]
            funspace = Funspace(polytopetype, polytopedim, kform, dofnumber)
            print(funspace.__dict__)

    def test_cubesquare(self):
        polytopetype = Polytopetype.cube
        polytopedim = Polytopedimension.dim2
        kform = Kform.zeroform
        listdofnumbertest = calcdof(polytopetype, polytopedim, degreemaxtest=5)
        print(listdofnumbertest)
        for i in range(0, len(listdofnumbertest)):
            dofnumber = listdofnumbertest[i]
            funspace = Funspace(polytopetype, polytopedim, kform, dofnumber)
            print(funspace.__dict__)

    def test_cubecube(self):
        polytopetype = Polytopetype.cube
        polytopedim = Polytopedimension.dim3
        kform = Kform.zeroform
        listdofnumbertest = calcdof(polytopetype, polytopedim, degreemaxtest=5)
        print(listdofnumbertest)
        for i in range(0, len(listdofnumbertest)):
            dofnumber = listdofnumbertest[i]
            funspace = Funspace(polytopetype, polytopedim, kform, dofnumber)
            print(funspace.__dict__)


def calcdof(polytopetype,polytopedimension,degreemaxtest):

    listdof = []

    if polytopetype.name == Polytopetype.simplex.name:
        for i in range(1, degreemaxtest):
            listdof.append(comb(polytopedimension.value + i, i))
        return listdof

    elif polytopetype.name == Polytopetype.cube.name:
        for i in range(1,degreemaxtest):
            listdof.append(pow(i+1,polytopedimension.value))
        return listdof


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FunspaceTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
