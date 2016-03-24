from sympy import*
import pickle
import random
from fephysics.stiffnessmatrix import*
import os
from readfreecadtopy import*
import numpy as np

def mappingfun(modelstiffnessmatrix,coord):
    return lambdify(coord,modelstiffnessmatrix, "numpy")


def main():

    for filename in os.listdir("c:/WorkingDirectory_Spyder/GIT_KFE/fephysics"):
        if filename == "libraryElemente8.p":
            file="c:/WorkingDirectory_Spyder/GIT_KFE/fephysics/"+"libraryElemente8.p"
            test = pickle.load(open(file, "rb" ))

    coord =[]
    for i in range(len(test[1].coord[0,:])):
        for j in range(test[1].dimension):
            coord.append(test[1].coord[i,j])

    mapping2D = mappingfun(factor(test[0]),coord)
    K= mapping2D(1,4,5,6)
    NElist = readfctopy("save.p")
    a=2
    numdofpernode = 2
    globalstiffnessmatrix = np.zeros((len(NElist[0])*2,len(NElist[0])*2))

    for i in range(0,len(NElist[1])):
        K = mapping2D(NElist[1][i].vertice1.coordinates[0],
                    NElist[1][i].vertice1.coordinates[1],
                    NElist[1][i].vertice2.coordinates[0],
                    NElist[1][i].vertice2.coordinates[1])
        np.array(K.tolist()).astype(np.float64)
        for j in range(0,2):
            for k in range(0,2):
                indexV1 = NElist[1][i].vertice1.index
                indexV2 = NElist[1][i].vertice2.index
                globalstiffnessmatrix[indexV1+j,indexV1+k]= globalstiffnessmatrix[indexV1+j,indexV1+j]+K[j,k]
                globalstiffnessmatrix[indexV1+j,indexV2+k]= globalstiffnessmatrix[indexV1+j,indexV1+j]+K[j,k+2]
                globalstiffnessmatrix[indexV2+j,indexV2+k]= globalstiffnessmatrix[indexV2+j,indexV2+j]+K[j+2,k]
                globalstiffnessmatrix[indexV2+j,indexV2+k]= globalstiffnessmatrix[indexV2+j,indexV2+j]+K[j+2,k+2]

    a=2

    #assembling the different matrices




if __name__ == "__main__":
    main()

