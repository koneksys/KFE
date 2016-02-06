# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:29:48 2016

@author: User
"""

from scipy.special import comb


#Test the class
#the term parametric describes any system of equations that gives one set o equations
#explicitly in terms of a second set of independent variables (the parameters)
class Polytope_Factory: 
    def getpolytope(self, Category, DimPolytope):
        if Category == 'simplex': 
            return Simplex(DimPolytope) 
        if Category == 'cube': 
            return Cube(DimPolytope)



class Simplex:
    """
    Creates a simplex.

    Parameters
    ----------
    DimPolytope: The number of independant points to describe the figure
        
    Methods:
    -------
    getName : give the common name of the simplex 
    getTopologySet: Calculate the number of vertice, Edge and Face using  
    combinatorics formulae.
    
     Required import:
    -------
    from scipy.special import comb
    
    See Also
    --------
    n-Cube and Polytope Factory

    Examples
    --------
    >>> from numpy.polynomial import polynomial as P
    >>> P.polyline(1,-1)
    array([ 1, -1])
    >>> P.polyval(1, P.polyline(1,-1)) # should be 0
    0.0

    """

    _SimplexName=['point','line','triangle','tetrahedron']
    _MeshPoint=[1]
    _MeshLine=[1,[2,3],[-1,1]]
    _LineParam=[-1,1]
    _MeshTriangle=[1,[2,3,4],[[5,6],[6,7],[7,5]],[[0,0],[0,1],[1,0]]]
    _MeshTetrahedron = [1,[2,3,4,5],[[6,7,8],[8,9,10],[6,10,11],[7,9,11]],[[[5,6],[6,7],[7,5]],[[5,6],[6,7],[7,5]],[[5,6],[6,7],[7,5]],[[5,6],[6,7],[7,5]]]]
    
    def __init__(self, DimPolytope): 
        self.DimPolytope = DimPolytope
        self.Name = self._SimplexName[self.DimPolytope]
        self.NbVertice= comb(self.DimPolytope+1,1)
        self.NbEdge = comb(self.DimPolytope+1,2)
        self.NbFace = comb(self.DimPolytope+1,3)
            
    def getMesh(self):
        if self.Name == 'point':
            return self._MeshPoint
        elif self.Name == 'line':
            return self._MeshLine
        elif self.Name == 'triangle':
            return self._MeshTriangle
        elif self.Name == 'tetrahedron':
            return self._MeshTetrahedron
            
   
class Cube: 
    def __init__(self, DimPolytope): 
        print "Currently no support for cube" 



        
 
 