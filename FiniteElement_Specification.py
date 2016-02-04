# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:22:35 2016

@author: User
"""
#https://jszarazi@bitbucket.org/jszarazi/kfe.git
#
#Specification = {'Quantity_type':'vector','Topology':{'Polytope':'Simplex','Dim':2 },;
#'1Face': {'FD':1,'PE':1,'NC':1},'0Face': {'FD':1,'PE':1,'NC':1}}

#Space dimension (DimSpace) is the number of parameters needed to specify the position
#of a particular point/Vertice. Space has n dimenson when n coordinates are required.

#Dimension of a polytope (DimPolytope) is defined to be a convex hull in some Euclidean space m
# of a set of n+1 points called vertices provided these points are independent
#in the sense that they are not collinear.



from Polytope_V4 import *


def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format((", ".join(valid_options)))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

def DOF_calculator(Face)


class FE_Specification:
    Valid_Polytope=("simplex","cube")
    Valid_DimPolytope=("0","1","2","3")
    Valid_DimSpace=("1","2","3")    
    Valid_ListReq_0Face=("pe","fd")
    Valid_ListReq_0FaceComb=("0","1")
    Valid_ListReq_1Face=("pe","fd")
    Valid_ListReq_1FaceComb=("0","1","2","3","4")
    Valid_FuncTypeList=("scalar","vector")
    
    def __init__(self):
                
        self.Polytope=None
        self.DimPolytope=None
        self.DimSpace=None
        self.FunctionSpaceType=None
        self.FunctionReq_0Face=[]
        self.FunctionReq_1Face=[]
        self.FunctionReq_2Face=[]
        self.FuncType= None
        self.NbDOF= None
        
   
    def prompt_init(self):
      
        self.Polytope = get_valid_input(
                'Enter the Polytope Type',
                self.Valid_Polytope)
                
        self.DimPolytope = int(get_valid_input(
                "Enter Dimension of Polytope",
                self.Valid_DimPolytope))
                
        self.DimSpace = int(get_valid_input(
                "Enter Space Dimension",
                self.Valid_DimSpace))
                
        if self.DimPolytope>self.DimSpace:
            print "Space Dimension should be greater or equal to Polytope dimension"
            self.DimSpace = int(get_valid_input(
                "Enter Valid Space Dimension",
                self.Valid_DimSpace))
                        
        self.FuncType = get_valid_input(
                "Enter Space Dimension",
                self.Valid_FuncTypeList) 
             
        for i in range (0,len(self.Valid_ListReq_0Face)):
            self.FunctionReq_0Face.extend([self.Valid_ListReq_0Face[i], 
                                           int(get_valid_input(
                "evaluation on 0-Face of type  "+self.Valid_ListReq_0Face[i],
                self.Valid_ListReq_0FaceComb))])       
        
        for i in range (0,len(self.Valid_ListReq_1Face)):
            self.FunctionReq_1Face.extend([self.Valid_ListReq_1Face[i], 
                                           int(get_valid_input(
                "evaluation on 0-Face of type  "+self.Valid_ListReq_1Face[i],
                self.Valid_ListReq_1FaceComb))]) 
         #Calculate the number of Degree of Freedom
        
         
         
class Finite_Element:
    self.Polytope=Simplex(2)
    
    pass
  
    def __init__(self, FE_Specification):
        self.FE_Specification= FE_Specification
        

import Polytope
 
def GenerateFE(FE_Specification):
    #generate the polytope
        PolyFac = Polytope_Factory()
        PolytopeFE = PolyFac.getPolytope(FE_Specification.Polytope, 
                                         FE_Specification.DimPolytope)
    #generate the functional space
    #calculate the number of degree of freedom
    #it depend also whether we have scalar or vector
        
A=[]        
for i in range(0,2):
    A.append(FEM.FunctionReq_0Face[2*i+1])
    B=sum(A)
                
        
        
        FunFac=FunctionSpace_Factory()
                   
          
           if FE_Specification.FuncType == 'Scalar':
               ScaSub=FunFac.get(1)
               #Calculate 
               ScaSub.getFunction('Monomial',1,2)
               ScaSub.getDerivative
           
           # from FiniteElement_Specification import *
           # testSpec1=FE_Specification()
           # testSpec1.set_Polytope('Simplex',1)
           # testSpec1.set_DimSpace(2)
           # testSpec1.__dict__
            #  from Polytope_V4 import *
           # A=GenerateFE(testSpec1)
        
#   def getShapeFunction(self):
 #       Polytope = PolyFac.getPolytope(self.FE_Specification.Polytope, self.FE_Specification.DimPolytope)
        

#to calculate the shape function we need to read the specification which means that
# we have first to calculate the number of degrees of freedom based upon the 
#type of DOF and the topological element. Based on this we can define what function 
# we need to choose to represent these degrees of freedoms. We then represent
#symbolicallty its values and its derivatives. 

    
