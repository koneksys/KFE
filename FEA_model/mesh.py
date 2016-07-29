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
            self.ListNeumann = [['NIST_NBC_1','NIST_NBC_2'],[1,0]]

        elif mathtype == Mathvartype.vector:
            if dimension == Geodimension.Geodim1:
                self.ListNeumann = [['NIST_NBC_1', 'NIST_NBC_2'], [1, 0]]
            elif (dimension == Geodimension.Geodim2) & (Topodimension.Topodim1 == Topodim):
                self.ListNeumann = [['NIST_NBC_1','NIST_NBC_2','NIST_NBC_3','NIST_NBC_4'], [1,0]]
                A = list(product((0, 1), repeat=Geodimension.Geodim2.value))
                B=[]
                C= ['Fx','Fy','Fx-Fy','planar']

                for i in range(0,len(A),1):
                    B.append('NIST_NBC_'+str(i))
                    self.ListNeumann = [C,B,A]

    def createBC(self,label,value,BCnodeindexlist):
        nblanguages=len(self.ListBCDirichlet)-1
        for i in self.ListBCDirichlet:
            for j in i:
                if j ==label:
                    return Boundary(label,self.ListBCDirichlet[nblanguages][i.index(j)],BCnodeindexlist)


class Boundary:
    def __init__(self,label,values,nodeindexes):
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
                    return Boundary(label,self.ListBCDirichlet[nblanguages][i.index(j)],BCnodeindexlist)




class NeumannBC:
    def __init__(self,dimension,mathtype,label,BCnodeindexlist):


        #search for the index of the label to assign the right condition to the node
        sizelist=len(self.ListBCDirichlet)
        k=0
        for i in range(0,sizelist,1):
            for element in self.ListBCDirichlet[i]:
                if element==label:
                    matchindex=self.ListBCDirichlet[i].index(label)
        #find the size of the list and then use the last "internal list" and use index to find the right condition

        self.DBCvalue=self.ListBCDirichlet[sizelist-1][matchindex]
        self.DBC=[label,self.DBCvalue,BCnodeindexlist]


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

    #coordinate are read from the input deck file or the mesh file
    coordinatelist=[[0,1],[1,0],[2,0]]
    edge2nodelist=[[1,2],[2,3],[1,4],[4,5],[4,2],[5,3],[2,5]]
    #coordinate are read from the input deck with a specific vocabulary or defined using the graphical user interface
    Rollerselection=[1,3]
    NBCnodeselection=[2]

    #the dimension of the problem is set
    dimension=Geodimension.Geodim2
    #the mathtype of the physics variable is set
    displacement=Mathvartype.vector

    nl_1=Nodelist(coordinatelist)
    el_2=Edgelist(edge2nodelist)
    propel1=ElementProperty(12,132)
    propel2=ElementProperty(12,40)
    BCD=BCDirichlet(dimension,displacement)
    a=BCD.createBC('roller',[2,4])
    BCD2=BCDirichlet(dimension,displacement)
    b=BCD.createBC('pin',0)
    bmodel=model(1,2,3)
    c=bmodel.funmodel
    a=2


if __name__ == "__main__":
    main()
