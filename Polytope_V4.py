# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:29:48 2016

@author: User
"""

from scipy.special import comb

class Polytope:
    pass


class Polytope_Factory: 
    def getPolytope(self, Category, Dimension): 
        if Category == 'Simplex': 
            return Simplex(Category, Dimension) 
        if Category == 'Cube': 
            return Cube(Category, Dimension)

#Test the class


class Simplex:
    _SimplexName=['point','line','triangle','tetrahedron']
    _MeshPoint=[1]
    _MeshLine=[1,[2,3]]
    _MeshTriangle=[1,[2,3,4],[[5,6],[6,7],[7,5]]]
    _MeshTetrahedron = [1,[2,3,4,5],[[6,7,8],[8,9,10],[6,10,11],[7,9,11]],[[[5,6],[6,7],[7,5]],[[5,6],[6,7],[7,5]],[[5,6],[6,7],[7,5]],[[5,6],[6,7],[7,5]]]]
    
    def __init__(self, Category, Dimension): 
        self.Category= Category        
        self.Dimension = Dimension
        self.name = self._SimplexName[self.Dimension]
        self.NbVertice= comb(self.Dimension+1,1)
        self.NbEdge = comb(self.Dimension+1,2)
        self.NbFace = comb(self.Dimension+1,3) 
            
    def getMesh(self):
        if self.name == 'point':
            return self._MeshPoint
        elif self.name == 'line':
            return self._MeshLine
        elif self.name == 'triangle':
            return self._MeshTriangle
        elif self.name == 'tetrahedron':
            return self._MeshTetrahedron
            

        
class Cube: 
    def __init__(self, Dimension): 
        print "Currently no support for cube" 



        


 
 