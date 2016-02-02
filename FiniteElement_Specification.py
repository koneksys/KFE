# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:22:35 2016

@author: User
"""
#https://jszarazi@bitbucket.org/jszarazi/kfe.git
#
#Specification = {'Quantity_type':'vector','Topology':{'Polytope':'Simplex','Dim':2 },;
#'1Face': {'FD':1,'PE':1,'NC':1},'0Face': {'FD':1,'PE':1,'NC':1}}

#Space dimension is the number of parameters needed to specify the position
#of a particular point. Space has n dimenson when n coordinates are required.

#Dimension of a polytope is defined to be a convex hull in some Euclidean space m
# of a set of n+1 points called vertices provided these points are independent
#in the sense that they are not collinear.


class FE_Specification:
    PolytopeAvail=['Simplex','Cube']
    ListReq_0Face=['PE','FD']
    ListReq_1Face= ListReq_0Face
    FuncTypeList=['Scalar','Vector','PseudoScalar','PseudoVector']
    
    def __init__(self):
        self.Polytope=None
        self.DimPolytope=None
        self.DimSpace=None
        self.FunctionSpaceType=None
        self.FunctionReq_0Face=None
        self.FunctionReq_1Face=None
        self.FunctionReq_2Face=None
        self.FuncType= None
        
    def set_Polytope(self,Polytope,DimPolytope):
        if (1<=DimPolytope<=3) & (Polytope in self.PolytopeAvail):  
            self.Polytope = Polytope
            self.DimPolytope= DimPolytope
        else:
            print 'only Simplex and Cube available or check dim = 1 or 2 or 3'
            
            
    def set_DimSpace(self,DimSpace):
        if (1<=DimSpace<=3):
            self.DimSpace=DimSpace
        else:
            print 'Support only for 1D, 2D, 3D, please give a number between 1 and 3'
            self.DimSpace=None
            
  #One implementation set_FaceReq is probably possible          
    def set_FaceReq_0Face(self,ReqFace0):
        if not len(ReqFace0)==len(self.ListReq_0Face):
            print 'give list of 2 arg - Arg1: PE (Point Evaluation) - Arg2: FD (First derivative)'
        elif (max(ReqFace0)<=1) & (min(ReqFace0)>=0):
            if ReqFace0[0]==0 and ReqFace0[1]==0:
                self.FunctionReq_0Face= None
            else:
                self.FunctionReq_0Face= [self.ListReq_0Face,ReqFace0]            
        else:
            print 'only 0 or 1 is accepted'
    
    def set_FaceReq_1Face(self,ReqFace1):
        if not len(ReqFace1)==len(self.ListReq_1Face):
            print 'give list of 4 arg - Arg1: PE (Point Evaluation) Arg2: FD (First derivative)'
        elif ReqFace1[0]==ReqFace1[1]:
            if ReqFace1[0]==0 and ReqFace1[1]==0:
                self.FunctionReq_1Face=None
            else:
                self.FunctionReq_1Face = [self.ListReq_1Face,ReqFace1]
        else:
            print 'PE=FD number of point evaluation has to be equal to number of derivative.'

    def set_FuncType(self,FuncType):
        if FuncType in self.FuncTypeList:
            self.FuncType=FuncType
        else:
            print 'Following list is provided'+''.join(self.FuncTypeList)
 
   
 
       
class Finite_Element:
    
    def __init__(self, FE_Specification):
        self.FE_Specification= FE_Specification
    
    

    
