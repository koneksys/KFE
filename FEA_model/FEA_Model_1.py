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



#we have a list of feat
from enum import Enum
from itertools import product


class Mathvartype(Enum):
    scalar = 1
    vector = 2
    tensor = 3


class Geodimension(Enum):
    Geodim1 = 1
    Geodim2 = 2
    Geodim3 = 3


class Topodimension(Enum):
    Topodim0 = 0
    Topodim1 = 1
    Topodim2 = 2
    Topodim3 = 3

#we are reading an input deck from a specific software
#the class should provide a method where the softwarename is provided,the name of the boundary
#condition is given and then it translate to the appropriate boundary vector.
#another input would be the index of the associate node.
#there are two options: the first option is to create a function in space and then create a method
#which will label the mesh elements


class BCNeumann:
    def __init__(self, dimension, Topodim, mathtype):
        if mathtype == Mathvartype.scalar:
            self.ListNeumann = [['NIST_NBC_1'],[1]]

        elif mathtype == Mathvartype.vector:
            if dimension == Geodimension.Geodim1:
                self.ListNeumann = [['NIST_NBC_1'], [1]]
            elif (dimension == Geodimension.Geodim2) & (Topodimension.Topodim1 == Topodim):
                self.ListNeumann = [['NIST_NBC_1','NIST_NBC_2'],['Fx','Fy'], [[1,0],[0,1]]]

    def createBC(self,label,value,BCnodeindexlist):
        nblanguages=len(self.ListNeumann)-1
        for i in self.ListNeumann:
            for j in i:
                if j ==label:
                    k = self.ListNeumann[nblanguages][i.index(j)]
                    l=range(len(k))
                    for m in k:
                        l[m]=value*m
                    return Boundary(label,BCnodeindexlist,l)


class Boundary:
    def __init__(self,label,nodeindexes,values):
        self.label=label
        self.nodeindexes=nodeindexes
        self.values=values


class BCDirichlet:
    def __init__(self,dimension,mathtype):
        #self.label=label
        if mathtype == Mathvartype.scalar:
            self.ListBCDirichlet = [['NIST_BCD_1','NIST_BCD_2'],[1,0]]

        elif (mathtype == Mathvartype.vector)&(dimension == Geodimension.Geodim1):
            self.ListBCDirichlet = [['NIST_BCD_1','NIST_BCD_2'],[1,0]]

        elif (mathtype == Mathvartype.vector)&(dimension == Geodimension.Geodim2):
            A = list(product((0, 1),repeat=Geodimension.Geodim2.value))
            B = []
            C= ['pin','roller','','planar']
            for i in range(0,len(A),1):
                B.append('NIST_BCD_'+str(i))
            self.ListBCDirichlet = [C,B,A]

        elif (mathtype == Mathvartype.vector)&(dimension == Geodimension.Geodim3):
            A = list(product((0, 1),repeat=Geodimension.Geodim3.value))
            B = []
            for i in range(0,len(A),1):
                B.append('NISTLabel'+str(i))
            self.ListBCDirichlet = [B,A]

    def createBC(self,label,BCnodeindexlist):
        nblanguages=len(self.ListBCDirichlet)-1
        for i in self.ListBCDirichlet:
            for j in i:
                if j ==label:
                    return Boundary(label,BCnodeindexlist,self.ListBCDirichlet[nblanguages][i.index(j)])





#an input is characterized by its variable/mathtype/functional


class AbstractInput:
    pass

class Cellintegral:
    pass

class exterior_facet_integral:
    pass

class interior_facet_integral:
    pass



class ElementProperty(AbstractInput):
    def __init__(self, Emodul,Area):
            self.Emodul=Emodul#scalar
            self.Area=Area#scalar
            #the element properties comes from the constitutive equation

class Problem:
    def __init__(self, Problemtype,Problemdimension, AbstractConstraint):
        if Problemtype == 1:
            pass


#the element of the FEA problem are lines thus defined by edgelist indexes, probably just to add a label in the edgelist attributes""
#from where do I get those element properties?
#what variable do I assign to the constraint?
#in the truss case the surface vector remain a scalar, in 2D problem that surface will be represented as a thickness.
#can someone of providing the vector parameters as a function of modeling dimension
#different level of abstraction - problem/physics/mathematics


#we need to implement a function to add information on the nodelist about the boundary conditions
#we need
def main():

    #the dimension of the problem is set
    dimension=Geodimension.Geodim2
    #the mathtype of the physics variable is set
    displacement=Mathvartype.vector
    force=Mathvartype.vector
    linedimension=Topodimension.Topodim1

    propel1=ElementProperty(12,132)
    propel2=ElementProperty(12,40)
    BCD=BCDirichlet(dimension,displacement)
    a=BCD.createBC('roller',[2,4])
    b=BCD.createBC('pin',0)
    NBC=BCNeumann(dimension,linedimension,force)
    d=NBC.createBC('Fy',-10000,1)
    breakvalue=4


if __name__ == "__main__":
    main()
