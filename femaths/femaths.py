# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 09:41:13 2016

@author: User
"""
from scipy.special import comb
from funreq import Funreq
from polytope import Polytope
from funspace import Funspace, funcube, funsimplex


class Femaths:
 pass

def numdofcal(polytope, *args):
    print(polytope)
    listreq = []
    for elem in args:
        listreq.append(elem)


    #return the number of requirements associated with finite element
    numreq = len(listreq)
    numdofreq = 0

    for i in range(0,numreq):
        if listreq[i].doftype == 0:
            numdofreq = numdofreq + (listreq[i].dofnumber)*\
                                    polytope.listnumface[listreq[i].facedim]
        #if the requirements are of type point evaluation
        #if the requirements are of type first derivative
        if listreq[i].doftype == 1:
            return numdofreq*polytope.polytopedim

def main():

    polytopetype1 = 'cube'
    polytopedimension1 = 1
    fieldtype = 'scalar'
    simplex1 = Polytope(polytopetype1, polytopedimension1)
    doftype1 = 0
    dofnumber1 = 1
    facedim1 = 0
    doftype2 = 1
    dofnumber2 = 1
    facedim2 = 0
    dofnumber3 = 2
    facedim3 = 1
    funreq1 = Funreq(doftype1, dofnumber1, facedim1)
    funreq2 = Funreq(doftype2, dofnumber2, facedim2)
    funreq3 = Funreq(doftype1, dofnumber3, facedim3)
    print(funcube(2,0,1,4))
    print(simplex1.__dict__)
    print(funreq1.__dict__)
    A1 = numdofcal(simplex1,funreq1,funreq2,funreq3)
    print(A1)



if __name__ == "__main__":
    main()
