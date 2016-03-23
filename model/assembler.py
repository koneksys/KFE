from sympy import*
import pickle
import random
from fephysics.stiffnessmatrix import*
import os

def main():

    for filename in os.listdir("c:/WorkingDirectory_Spyder/GIT_KFE/fephysics"):
        if filename == "libraryElementj2.p":
            file="c:/WorkingDirectory_Spyder/GIT_KFE/fephysics/"+"libraryElementj2.p"
            test = pickle.load(open(file, "rb" ))

    a=2

if __name__ == "__main__":
    main()

