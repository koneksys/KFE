# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:00:59 2016

@author: User
"""

#In mathematics, a function space is a set of functions of a given 
#kind from a set X to a set Y. It is called a space because 
#in many applications it is a topological space (including metric spaces)
#, a vector space, or both."""


#A vector polynomial has x-component composed of the same basis with
#different coefficients
#A scalar function is composed of:
#    - its coefficient (vector component)
#    - its Basis Function (vector basis)

#The scalar product of the two gives the scalar function,

#This can be extended to any dimension:
#in our case we have actually: FuncDim scalar = [1], vector=[N] which we

from sympy import*
from sympy.abc import alpha
from sympy.polys.monomials import itermonomials

class FunctionSpace:
    pass


class FunctionSpace_Factory:
    def get(self, FuncDim):
        if FuncDim == 1:
            return Scalar_Subspace()
        elif FuncDim >= 2:
            return Vector_Subspace()
            
class Scalar_Subspace:
    _x,_y,_z=symbols('x y z')
    __BasisFactory=[]
    __Basis=[]
    __BasisAsList=[]  
    __CoefSymb=[]
    __FuncMat=[]
    __Func=[]
    
    def __init__(self):
        self.Function = None
        self.NbVariable = None
        self.NbDOF = None
        self.BasisType = None
        self.Basis = None
        self.Derivative=None
                       
    def getFunction(self,BasisType, NbVariable,Degree):
        #set entry values to atrributes        
        self.BasisType=BasisType
        self.NbVariable=NbVariable
        self.Degree=Degree
        #generate Basis Factory
        __BasisFactory=BasisFunc_Factory()
        #generate Basis Function            
        __Basis=__BasisFactory.get(BasisType,NbVariable)
        #set the result values to attribute
        self.Basis=__Basis.get(Degree)
        self.NbDOF = len(self.Basis)
        #transform the Basis set into a list
        __BasisAsList = list(self.Basis)
        #generate symbolic vector component/ polynomial coefficient
        __CoefSymb = MatrixSymbol('alpha',1,self.NbDOF)
        __FuncMat= Matrix(__CoefSymb)*Matrix(__BasisAsList)
        self.Function=__FuncMat[0]
        self.Derivative=None
        
    def getDerivative(self):
        if self.Function==None:
            print 'No function to derive, apply get method first'
        elif self.NbVariable==1:
            self.Derivative=diff(self.Function,self._x,1)
            return self.Derivative
            print 'Derivate has been calculated'
        else:
            print 'Nothing happened'
    #the method eval_var calculate the basis for a specific coordinate
    #the vector component, polynomial coefficient are still unknown
    def evalFunc(self,value):
        if self.Function==None:
            print 'No function to evaluate, apply get method first'
        if len(value)==1:
            __Func=self.Function            
            return __Func.subs(self._x,value[0])
        else:
            print 'multivariate not supported for evaluation'
            
    def evalDerivative(self,value):
        if self.Derivative==None:
            print 'No derivative to evaluate, apply get method first'
        if len(value)==1:
            return self.Derivative.subs(self._x,value[0])
        else:
            print 'multivariate not supported for evaluation'
            
            
#Test: 
# FunFac=FunctionSpace_Factory()
# ScaSub=FunFac.get(1)
# ScaSub.getFunction('Monomial',1,2)
# ScaSub.__dict__       
# ScaSub.getDerivative    
   
  



#For now we only consider 1 to 3 dimensional monomial basis
class BasisFunc_Factory:
    def get(self, BasisType, NbVariable): 
        if BasisType == 'Monomial': 
            return MonomialBasis(BasisType, NbVariable) 
        if BasisType == 'trigonometric': 
            return 'is not supported'


class MonomialBasis:
    _x,_y,_z=symbols('x y z')
    
    def __init__(self, BasisType,NbVariable):
        self.BasisType = BasisType
        self.NbVariable = NbVariable
        self.NbDOF = None
        self.Basis= None
        
    def get(self, Degree):
         if self.NbVariable==1:
            self.Basis = itermonomials([self._x], Degree)
            self.NbDOF = len(self.Basis)
            return self.Basis
            
         elif self.NbVariable==2:
            self.Basis = itermonomials([self._x, self._y], Degree)
            self.NbDOF = len(self.Basis)
            return self.Basis
            
         elif self.NbVariable==3: 
            self.Basis = itermonomials([self._x, self._y, self._z], Degree)
            self.NbDOF = len(self.Basis)
            return self.Basis
            
         else:
             print 'support only 1 to 3 dimensional - give a number between 1 and 3'
    

"""Test Class: Monomial Basis"""
N=BasisFunc_Factory()
T=N.get('Monomial',2)
P=T.get(1)
            
