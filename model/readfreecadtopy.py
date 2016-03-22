import pickle
from femaths.femesh import Vertice, Edge


def main():

    nodeedgelist = pickle.load(open("save.p", "rb" ))
    nodelist = nodeedgelist[0]
    edgelist = nodeedgelist[1]
    a =2

    for i in range(0,len(edgelist)):
        for j in range(0,len(nodelist)):
            test1x = edgelist[i].vertice1.coordinates[0] == nodelist[j].coordinates[0]
            test1y = edgelist[i].vertice1.coordinates[1] == nodelist[j].coordinates[1]
            test1z = edgelist[i].vertice1.coordinates[2] == nodelist[j].coordinates[2]
            test2x = edgelist[i].vertice2.coordinates[0] == nodelist[j].coordinates[0]
            test2y = edgelist[i].vertice2.coordinates[1] == nodelist[j].coordinates[1]
            test2z = edgelist[i].vertice2.coordinates[2] == nodelist[j].coordinates[2]

            if test1x and test1y and test1z:
                edgelist[i].vertice1.index = nodelist[j].index[0]
            if test2x and test2y and test2z:
                edgelist[i].vertice2.index = nodelist[j].index[0]

    a =2

if __name__ == "__main__":
    main()
