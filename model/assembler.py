from sympy import *
import pickle
import random
from fephysics.stiffnessmatrix import *
import os
from model.readfreecadtopy import *
import numpy as np


def mappingfun(modelstiffnessmatrix, coord):
    return lambdify(coord, modelstiffnessmatrix, "numpy")


class Feanalysis:
    def __init__(self, meshfile, physicsvarlist, analysistype):
        pass
        # we need to read the meshfile in order to know the dimension
        # and the type of FE-geometry we want to describe the physics with
        # Therefore the dimension of the mesh is given by the coordinate dimension of the node coordinate
        # We know that we could associate the variable with diagram and that depending on the discretization
        # of the variable we can either use the primal functional, dual functional, HR or WHZ functional.
        # this is for the category of equation of type dirichlet problem-
        # the process for 1D problems in 1D-2D-3D is to first create the geometry or mesh describing the geometric
        # of interest. The second step is to transform that geometry file into the general topology mesh data structure
        # and save it as python object in a analysis directory.
        # library elements should be in advance stored as physics independant library elements - a line
        # can be implemented in 1D-2D-3D so we have 3 combinatiosn - futhermore DOF could be scalars or vectors.
        # we know also that the resulting will depend on the finite element type for the description of the physics
        # variable and/or the geometry. We need to create an efficient data processing flow.


def main():
    for filename in os.listdir("c:/WorkingDirectory_Spyder/GIT_KFE/fephysics"):
        if filename == "libraryElementh1.p":
            file = "c:/WorkingDirectory_Spyder/GIT_KFE/fephysics/" + "libraryElementh1.p"
            test = pickle.load(open(file, "rb"))
    #
    coord = []
    for i in range(len(test[1].coord[0, :])):
        for j in range(test[1].dimension):
            coord.append(test[1].coord[i, j])

    mapping2D = mappingfun(factor(test[0]), coord)
    K = mapping2D(1, 4, 5, 6)
    B=K[0]
    NElist = readfctopy("save.p")
    a = 2
    numdofpernode = 2
    nbDOFperNode = 2
    globalstiffnessmatrix = np.zeros((len(NElist[0]) * nbDOFperNode, len(NElist[0]) * nbDOFperNode))

    for i in range(0, len(NElist[1])):
        K = mapping2D(NElist[1][i].vertice1.coordinates[0],
                      NElist[1][i].vertice1.coordinates[1],
                      NElist[1][i].vertice2.coordinates[0],
                      NElist[1][i].vertice2.coordinates[1])
        np.array(K.tolist()).astype(np.float64)
        for j in range(0, 2):
            for k in range(0, 2):
                indexV1 = NElist[1][i].vertice1.index
                indexV2 = NElist[1][i].vertice2.index
                globalstiffnessmatrix[nbDOFperNode * indexV1 + j, nbDOFperNode * indexV1 + k] \
                    = np.add(globalstiffnessmatrix[nbDOFperNode * indexV1 + j, nbDOFperNode * indexV1 + k], K[j, k])
                globalstiffnessmatrix[nbDOFperNode * indexV1 + j, nbDOFperNode * indexV2 + k] = \
                    np.add(globalstiffnessmatrix[nbDOFperNode * indexV1 + j, nbDOFperNode * indexV2 + k], K[j, k + 2])
                globalstiffnessmatrix[nbDOFperNode * indexV2 + j, nbDOFperNode * indexV1 + k] = \
                    np.add(globalstiffnessmatrix[nbDOFperNode * indexV2 + j, nbDOFperNode * indexV1 + k], K[j + 2, k])
                globalstiffnessmatrix[nbDOFperNode * indexV2 + j, nbDOFperNode * indexV2 + k] = \
                    np.add(globalstiffnessmatrix[nbDOFperNode * indexV2 + j, nbDOFperNode * indexV2 + k],
                           K[j + 2, k + 2])

    a = 2

    # assembling the different matrices


# Integrating the boundary conditions - we need a selection and visualization mechanism?



if __name__ == "__main__":
    main()
