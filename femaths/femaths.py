# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 09:41:13 2016

@author: User
"""
from scipy.special import comb
from funreq import Funreq, Fieldtype, Doftype, Meshobjecttype
from polytope import Polytope, Polytopedimension, Polytopetype
from funspace import Funspace, Kform
from enum import Enum




#the problem is that you require the nbofDof to instantiate the element funspace...
#the function can be external and associated to main.

class Femaths:
    def __init__(self, polytope, funspace, listreq):

        test1 = isinstance(polytope, Polytope)
        test2 = isinstance(funspace, Funspace)
        #testing that the list is composed of element of type Funrec
        test3 = True
        iterlistreq = iter(listreq)
        for i in iterlistreq:
            test3 = test3 and isinstance(i, Funreq)

        #final test = arguments are OK
        if test1 == True and test2 == True and test3 == True:
            self.polytope = polytope
            self.funspace = funspace
            self.listreq = listreq

            equation = 0
            for i in range(0, len(listreq)):

                if listreq[i].doftype == Doftype.pointevaluation:
                    if polytope.polytopedim >= listreq[i].facedim:
                        ndof = ndof + listreq[i].dofnumber * \
                                  polytope.listnumface[listreq[i].facedim]



        else:
            raise NameError('first argument is an object of type Polytope, second '
                        'argument is of type Funspace '
                            'and the third is a list composed of objects of type Funreq')

        #the goal is to calculate the shape functions


def numberdof(polytope, listreq):
    #TO DO verify whether the problem can be represented or not.
    #verify that first argument is of type polytope
    #it could return a validated list
    #it could calculate the coordinate on the polytope based upon the requirement
    test1 = isinstance(polytope, Polytope)

    #testing that the list is composed of element of type Funrec
    test2 = True
    iterlistreq = iter(listreq)
    for i in iterlistreq:
        test2 = test2 and isinstance(i, Funreq)

    #final test = arguments are OK
    if test1 == True and test2 == True:
    #so now we have the requirement list...which are not sorted...therefore someone
    #should start by reading the requirement...it should be more a requirement based reading...
        ndof = 0
        for i in range (0, len(listreq)):
            #reading of point evaluation requirements
            if listreq[i].doftype == Doftype.pointevaluation:

                if polytope.polytopedim >= listreq[i].facedim:
                    ndof = ndof + listreq[i].dofnumber * \
                                  polytope.listnumface[listreq[i].facedim]

                else:
                    raise NameError('requirements cant be applied to polytope. use polytope instance with'
                                    'appropriate dimension')

            if listreq[i].doftype == Doftype.firstderivative:

                if polytope.polytopedim >= listreq[i].facedim:
                    ndof = ndof + polytope.polytopedim * \
                                  listreq[i].dofnumber * \
                                  polytope.listnumface[listreq[i].facedim]

                else:
                    raise NameError('requirements cant be applied to polytope. use polytope instance with'
                                    'appropriate dimension')

        return ndof

    else:
        raise NameError('first argument is an object of type polytope, second '
                        'argument is a list composed of objects of type Funreq')


def main():

    polytopetype1 = Polytopetype.simplex
    polytopedimension1 = Polytopedimension.dim2
    fieldtype = Fieldtype.scalar
    kform1 = Kform.zeroform
    simplex1 = Polytope(polytopetype1, polytopedimension1)
    doftype1 = Doftype.pointevaluation
    dofnumber1 = 2
    facedim1 = Meshobjecttype.edge
    doftype2 = Doftype.pointevaluation
    dofnumber2 = 1
    facedim2 = Meshobjecttype.vertice
    doftype3 = Doftype.pointevaluation
    dofnumber3 = 1
    facedim3 = Meshobjecttype.face
    funreq1 = Funreq(doftype1, facedim1, dofnumber1)
    funreq2 = Funreq(doftype2, facedim2, dofnumber2)
    funreq3 = Funreq(doftype3, facedim3, dofnumber3)
    listreq = [funreq1, funreq2,funreq3]
    ndof = numberdof(simplex1, listreq)
    funspace1 = Funspace(polytopetype1, polytopedimension1, kform1, ndof)
    #femath = Femaths(polytope,funspace,listreq)
    print(simplex1.__dict__)
    print(funreq1.__dict__)
    print(funreq2.__dict__)
    print(listreq)
    print(ndof)
    print(funspace1.__dict__)


if __name__ == "__main__":
    main()
