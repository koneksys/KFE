# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 09:41:13 2016

@author: User
"""
from scipy.special import comb
from funreq import Funreq, Fieldtype, Doftype, Meshobjecttype
from polytope import Polygontype, Polygoncoordinate, Polytopetype, Polyhedrontype, Polytope
from enum import Enum
from femesh import Femesh, Vertice, Edge, Face, Paramrange
from funspace import Monomial, Tensorspace,funeval
from polytope import Polygontype, Polygoncoordinate, Polytopetype, Polyhedrontype, Polytope
from sympy import*

#the problem is that you require the nbofDof to instantiate the element funspace...
#the function can be external and associated to main.

class Femaths:
    def __init__(self, funspace, femesh):

        try:
            isinstance(femesh, Femesh)
            isinstance(funspace, Monomial) or isinstance(funspace,Tensorspace)
        except:
            raise NameError('1st argument of type Monomial or Tensorspace, 2nd arg of type Femesh')

        if not funspace.dofnumber == femesh.dofnumber:
            raise NameError('number of polynonmial == number of dof applied to femesh.')

        equationlist=[]
        for i in range(0, len(femesh.edgelist[0].interiorvertices)):
            localeq=[]
            localeq.append(femesh.edgelist[0].interiorvertices[i].index)
            for k in range(0,len(femesh.edgelist[0].interiorvertices[i].funreq)):
                localeq.extend([funspace.funeval(femesh.edgelist[0].interiorvertices[i].funreq[k] ,
                                                femesh.edgelist[0].interiorvertices[i].coordinates)])

            equationlist.append(localeq)

        for i in range(0,len(femesh.verticelist)):
            localeq=[]
            localeq.append(femesh.verticelist[i].index)
            for k in range(0,len(femesh.verticelist[i].funreq)):
                localeq.extend([funspace.funeval(femesh.verticelist[i].funreq[k],
                                                femesh.verticelist[i].coordinates)])

            equationlist.append(localeq)

        self.equationlist=equationlist

        dofnumber = femesh.dofnumber

        c = Matrix(MatrixSymbol('c', 1, dofnumber))
        from sympy.matrices import zeros
        vdmmatrix = zeros(dofnumber,dofnumber)

        index = 0
        for i in range(0,len(equationlist)):
            for k in range(1,len(equationlist[i])):
                index = index + 1
                seteq = equationlist[i][k].as_coefficients_dict()
                for l in range(0, dofnumber):
                    if c[0,l] in seteq:
                        vdmmatrix[index,l] = seteq(c[0,l])
                    else:
                        vdmmatrix[index,l] = 0

        self.vdmmatrix = vdmmatrix
"""
from sympy import*
coefvec = MatrixSymbol('c', 1, 6)
c=Matrix(coefvec)

A= c[0, 0] + c[0, 1]/2 + c[0, 2]/4 + c[0, 3]/8 + c[0, 4]/16 + c[0, 5]/32

A.as_coefficients_dict()
coefA=[]
SetA=A.as_coefficients_dict()
        dofnumber = femesh.dofnumber
        from sympy.matrices import zeros
        coefMatrix = zeros(dofnumber,dofnumber)
       #read coefficient of the equation and create a numerical matrix.
        for i in range(0, dofnumber):
            for k in range(0, dofnumber):
                if c[0,i] in
               for i in range(0,6):
    if c[0,i] in SetA:
        coefA.append(SetA[c[0,i]])
    else:
        coefA.append(0)



"""


"""coefA=[]
SetA=A.as_coefficients_dict()
for i in range(0,6):
    k=0
    for elem in SetA:
          if elem == c[0,i]:
              coefA.append(SetA.items()[k][1])
          k=k+1
        for i in range(0,6):
            for elem in B.as_coefficients_dict():
                if elem == c[0,i]
                    A[i]=

        listnew.items()[3][0]

        from sympy.matrices import zeros
        CoefMatrix=zeros(NbDOF,NbDOF)
"""

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

    doftype2 = Doftype.firstderivative
    facedim2 = Meshobjecttype.vertice
    dofnumber2 = 1
    funcreq2 = Funreq(doftype2, facedim2, dofnumber2)

    doftype3 = Doftype.pointevaluation
    facedim3 = Meshobjecttype.edge
    dofnumber3 = 1
    funcreq3 = Funreq(doftype3, facedim3, dofnumber3)

    doftype4 = Doftype.firstderivative
    facedim4 = Meshobjecttype.edge
    dofnumber4 = 1
    funcreq4 = Funreq(doftype4, facedim4, dofnumber4)
    funreqlist1 = [funcreq1,funcreq2,funcreq3,funcreq4]
    linemesh.applyfunreq(funreqlist1)
    poly1Dlinear_x = Monomial(1, 5, ['x'])
    femathline = Femaths(poly1Dlinear_x,linemesh)
    a=2



if __name__ == "__main__":
    main()
