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
class BCDirichlet:
    def __init__(self,dimension,mathtype):
        if mathtype == Mathvartype.scalar:
            self.ListBCDirichlet = [['NISTlabel1','NISTlabel2'],[1,0]]
        elif (mathtype == Mathvartype.vector)&(dimension == Geodimension.Geodim1):
            self.ListBCDirichlet = [['NISTlabel1','NISTlabel2'],[1,0]]
        elif (mathtype == Mathvartype.vector)&(dimension == Geodimension.Geodim2):
            A = list(product((0, 1),repeat=Geodimension.Geodim2.value))
            B = []
            C= ['pin','roller','','planar']
            for i in range(0,len(A),1):
                B.append('NISTLabel'+str(i))
            self.ListBCDirichlet = [C,B,A]
        elif (mathtype == Mathvartype.vector)&(dimension == Geodimension.Geodim3):
            A = list(product((0, 1),repeat=Geodimension.Geodim3.value))
            B = []
            for i in range(0,len(A),1):
                B.append('NISTLabel'+str(i))
            self.ListBCDirichlet = [B,A]



#an input is characterized by its variable/mathtype/functional

def funmodel(self,inputlist,outputlist,parameter):
        b=inputlist+outputlist*parameter
        return b

#we have three types of input, the distributed load, the kinematic constraint and the natural BC.
#to each of these three types we can assign a mutlinear functional.

class model:
    def __init__(self, inputlist,outputlist,parameter):
        self.inputlist=inputlist
        self.outputlist=outputlist
        self.parameter=parameter

    def funmodel(self):
        return funmodel(self.inputlist,self.outputlist,self.parameter)


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

class Edgelist:
    def __init__(self, edge2nodelist):
        self.dimension=1
        self.nbedge=len(edge2nodelist)
        self.Edgelist=[self.dimension,range(0,len(edge2nodelist),1),edge2nodelist]
        pass


class Nodelist:
    def __init__(self, coordinatelist):
        self.dimension = 0
        self.indexlist=range(0,len(coordinatelist))
        self.nodelist = [self.dimension,self.indexlist,coordinatelist]

#we need to implement a function to add information on the nodelist about the boundary conditions
#we need
def main():
    coordinatelist=[[0,1],[1,0],[2,0]]
    edge2nodelist=[[1,2],[2,3],[1,4],[4,5],[4,2],[5,3],[2,5]]

    dimension=Geodimension.Geodim2
    displacement=Mathvartype.vector
    nl_1=Nodelist(coordinatelist)
    el_2=Edgelist(edge2nodelist)
    propel1=ElementProperty(12,132)
    propel2=ElementProperty(12,40)
    bmodel=model(1,2,3)
    c=bmodel.funmodel
    testDC=BCDirichlet(dimension,displacement)
    a=2


if __name__ == "__main__":
    main()
