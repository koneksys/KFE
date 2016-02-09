
class Funreq:
    def __init__(self, doftype, dofnumber, facedim):

        listdof = ['pointevaluation', 'firstderivative',
                   'secconderivative', 'normalderivative',
                   'Facetangentvector', 'facenormalvector', 'interiormoment']

        listkface = ['vertice', 'edge', 'face', 'region']

        if (doftype == 0 or doftype == 1) and (facedim < 1) and (dofnumber > 1):
            raise NameError('only one degree of freedom is possible on vertice')


        self.facedim = facedim
        self.dofnumber = dofnumber
        self.doftype = doftype
        self.doftypename = listdof[doftype]
        self.meshobsjecttype = listkface[self.facedim]




def main():
    doftype1 = 1
    dofnumber1 = 1
    facedim1 = 0
    funcreq1 = Funreq(doftype1, dofnumber1, facedim1)
    print(funcreq1.__dict__)

if __name__ == "__main__":
    main()