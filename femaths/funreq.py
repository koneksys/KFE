
from enum import Enum


class Doftype(Enum):
    pointevaluation = 1
    firstderivative = 2
    secconderivative = 3
    normalderivative = 4
    facetangentvector = 5
    facenormalvector = 6
    interiormoment = 7


class Fieldtype(Enum):
    scalar = 1
    vector = 2


class Meshobjecttype(Enum):
    vertice = 0
    edge = 1
    face = 2
    volume = 3


class Funreq:
    def __init__(self, doftype, meshobjecttype, dofnumber):
        #may convert list as enum
        if isinstance(doftype, Doftype) and isinstance(meshobjecttype, Meshobjecttype):

            if (doftype.value == 0 or doftype.value == 1) and (meshobjecttype.value < 1) and (dofnumber > 1):
                raise NameError('only one degree of freedom is possible on vertice')

            self.info = [doftype, meshobjecttype]
            self.doftype = doftype
            self.doftypename = doftype.name
            self.facedim = meshobjecttype.value
            self.facename = meshobjecttype.name
            self.dofnumber = dofnumber

        else:
            raise NameError('argument 1 is of enum type Doftype, argument 2 is of enum facedim, argument 3 is integer')


def main():
    doftype1 = Doftype.pointevaluation
    facedim1 = Meshobjecttype.edge
    dofnumber1 = 3
    funcreq1 = Funreq(doftype1, facedim1, dofnumber1)
    print(funcreq1.__dict__)

if __name__ == "__main__":
    main()