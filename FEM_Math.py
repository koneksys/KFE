# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 09:41:13 2016

@author: User
"""
from scipy.special import comb

class FEM_Math:
    def __init__(self,polytopetype,dimpolytope,functionspacetype):
        
        self.polytope = Polytope(polytopetype,dimpolytope)
        self.polytope.get_topo()
        
        self.functionalspacetype = functionspacetype
        self.function = None
        #self.functionalspace=FunctionalSpace(functionspacetype)
        self.functionalrequirement=[]
        
        self.shapefunction = None
        self.nbdof = None
     
    def define_requirement(self, functionalrequirement):
        self.functionalrequirement.append(functionalrequirement)
        
    def get_function_space(self,nbdof):
        return self.functionspace
        
    def get_shapefunction(self):
        return self.shapefunction
     
    def display(self):
        return 2
        

class FunctionalRequirement:
      def __init__(self,doftype,dofnumber,meshobjecttype):
        
        self.doftype = doftype
        self.dofnumber = dofnumber
        self.meshobjecttype = meshobjecttype
        self.validation=None

      def validate(self):
         valid_doftype=['pointevaluation','firstderivative',
         'secconderivative','normalderivative','Facetangentvector',
         'facenormalvector','interiormoment']
         return valid_doftype
    
    
class Polytope:
    def __init__(self,polytopetype,dimpolytope):
        self.dimpolytope = dimpolytope
        self.polytopetype = polytopetype
        self.name = None
        self.numvertice = None
        self.numedge = None
        self.numface = None

    def get_topo(self):
        
        if self.polytopetype == 'simplex':
            
            simplexname=['point','line','triangle','tetrahedron']
            
            self.name = simplexname[self.dimpolytope]
            self.numvertice= comb(self.dimpolytope+1,1)
            self.numedge = comb(self.dimpolytope+1,2)
            self.numface = comb(self.dimpolytope+1,3)

        elif self.polytopetype == 'cube':
            
            cubename=['point','line','square','cube']
            self.name = cubename[self.dimpolytope]



class FunctionalSpace:
    pass


class ScalarSpace(FunctionalSpace):
    pass
