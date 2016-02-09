# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 19:29:48 2016

@author: User
"""

from scipy.special import comb, factorial


class Polytope:
    def __init__(self, polytopetype, polytopedim):
        self.polytopedim = polytopedim
        self.polytopetype = polytopetype
        self.name = None
        self.listnumface = []

        if self.polytopetype == 'simplex':

            simplexname = ['point', 'line', 'triangle', 'tetrahedron']
            self.name = simplexname[self.polytopedim]
            listnumface = []

            for i in range(0, self.polytopedim+1):
                listnumface.extend([comb(self.polytopedim + 1, i + 1)])

            self.listnumface = listnumface

        elif self.polytopetype == 'cube':

            cubename = ['point','line','square','cube']
            self.name = cubename[self.polytopedim]
            listnumface = []

            for i in range(0, self.polytopedim+1):
                listnumface.extend([pow(factorial(i)*factorial(self.polytopedim-i),-1)*
                                         factorial(self.polytopedim)*pow(2,self.polytopedim-i)])

            self.listnumface = listnumface



def main():
    polytopetype1 = 'simplex'
    polytopedim1 = 2
    simplex2 = Polytope(polytopetype1, polytopedim1)


    polytopetype2 = 'cube'
    polytopedim2 = 2
    cube2 = Polytope(polytopetype2, polytopedim2)



if __name__ == "__main__":
    main()
