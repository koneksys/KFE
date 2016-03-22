# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 09:41:13 2016

@author: User
"""
from scipy.special import comb
from femaths.funreq import Funreq, Fieldtype, Doftype, Meshobjecttype
from enum import Enum
from femaths.femesh import Femesh, Vertice, Edge, Face
from femaths.funspace import Monomials, Tensorspace,funeval
from femaths.polytope import Polygontype, Polygoncoordinate, Polytopetype, Polyhedrontype, Polytope
from sympy import*

#the problem is that you require the nbofDof to instantiate the element funspace...
#the function can be external and associated to main.

class Femath:
    def __init__(self, funspace, femesh):

        try:
            isinstance(femesh, Femesh)
            isinstance(funspace, Monomials) or isinstance(funspace, Tensorspace)
        except:
            raise NameError('1st argument of type Monomials or Tensorspace, 2nd arg of type Femesh')

        if not funspace.dofnumber == femesh.dofnumber:
            raise NameError('number of polynonmial == number of dof applied to femesh.')

        equationlist=[]
        infoshape = []
        for j in range(0,femesh.listnumface[1]):
            for i in range(0, len(femesh.edgelist[j].interiorvertices)):
                localeq=[]
                localeq.append(femesh.edgelist[j].interiorvertices[i].index)
                for k in range(0,len(femesh.edgelist[j].interiorvertices[i].funreq)):
                    localeq.extend([funspace.funeval(femesh.edgelist[j].interiorvertices[i].funreq[k] ,
                                                    femesh.edgelist[j].interiorvertices[i].coordinates)])
                    infoshape.append((femesh.edgelist[j].interiorvertices[i].index,
                                      femesh.edgelist[j].interiorvertices[i].funreq[k]))

                equationlist.append(localeq)

        for i in range(0,len(femesh.verticelist)):
            localeq=[]
            localeq.append(femesh.verticelist[i].index)
            for k in range(0,len(femesh.verticelist[i].funreq)):
                localeq.extend([funspace.funeval(femesh.verticelist[i].funreq[k],
                                                femesh.verticelist[i].coordinates)])
                infoshape.append((femesh.verticelist[i].index,
                                  femesh.verticelist[i].funreq[k]))

            equationlist.append(localeq)

        self.dofnumber = femesh.dofnumber
        self.listnumface = femesh.listnumface
        self.geometry = femesh.geometry
        self.var = funspace.var
        dofnumber = femesh.dofnumber

        c = Matrix(MatrixSymbol('c', 1, dofnumber))
        from sympy.matrices import zeros
        vdmmatrix = zeros(dofnumber,dofnumber)

        index = 0

        for i in range(0,len(equationlist)):
            for k in range(1,len(equationlist[i])):
                seteq = equationlist[i][k][0].as_coefficients_dict()
                for l in range(0, dofnumber):
                    if c[0,l] in seteq:
                        vdmmatrix[index,l] = seteq[c[0,l]]
                    else:
                        vdmmatrix[index,l] = 0
                index = index + 1

        shapefunlist=[]
        for i in range(0, dofnumber):
            shapefun = vdmmatrix.inv()[:,i].transpose()*Matrix(funspace.basis)
            shapefunlist.append((infoshape[i],shapefun[0]))

        #Store information of the shapefunction into the mesh.
        if len(femesh.listnumface) == 2:
            self.mesh = femesh.edgelist
            for i in range(0, len(shapefunlist)):
                if len(shapefunlist[i][0][0]) == 2:
                    for j in range(0, len(self.mesh[0].interiorvertices)):
                        if self.mesh[0].interiorvertices[j].index == shapefunlist[i][0][0]:
                            self.mesh[0].interiorvertices[j].shapefunction.append(shapefunlist[i][1])
                elif len(shapefunlist[i][0][0]) == 1:
                    if shapefunlist[i][0][0] == self.mesh[0].vertice1.index:
                        self.mesh[0].vertice1.shapefunction.append(shapefunlist[i][1])
                    elif shapefunlist[i][0][0] == self.mesh[0].vertice2.index:
                        self.mesh[0].vertice2.shapefunction.append(shapefunlist[i][1])

        self.shapefunlist = shapefunlist

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
    polyhermitte_x = Monomials(1, 5, ['x'])
    femathline = Femath(polyhermitte_x, linemesh)



    polytopetype2 = Polytopetype.polygon
    polygontype2 = Polygontype.triangle
    polyhedrontype2 = Polyhedrontype.nopolyhedron
    polytopecoord2 = Polygoncoordinate(polygontype2)
    triangle = Polytope(polytopetype2, polygontype2, polyhedrontype2, polytopecoord2)
    trianglemesh = Femesh(triangle)
    doftype5 = Doftype.pointevaluation
    facedim5 = Meshobjecttype.vertice
    dofnumber5 = 1
    funcreq5 = Funreq(doftype5, facedim5, dofnumber5)
    funreqlist2 = [funcreq5,funcreq3]
    trianglemesh.applyfunreq(funreqlist2)
    poly2Dlinear_xy = Monomials(2, 2, ['x','y'])
    femathtriangle = Femath(poly2Dlinear_xy, trianglemesh)
    breakpoint=2



if __name__ == "__main__":
    main()
