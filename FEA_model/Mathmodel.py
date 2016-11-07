"""
 KFE
 * http://www.koneksys.com/
 *
 * Copyright 2016 Koneksys
 * Released under the MIT license
 *
 * @author Jerome Szarazi (jerome.szarazi@koneksys.com)
 */
"""



import numpy as np




class Tensor:
    def __init__(self,rank,dimen):
        if isinstance(tensortype,list):
            self.tensortype=tensortype
            self.array=np.zeros([tensortype[0]*dimension+1, tensortype[1]*dimension+1])
        else:
            raise NameError('format should be tensor type = [r,q]')
    pass


class Polartensor(Tensor):
    pass


class Axialtensor(Tensor):
    pass


class Antisymmetricttensor(Tensor):
    pass



def main():

    tensor1=Polartensor([1,0],3)
    print len(tensor1.array)
    b=3

if __name__ == "__main__":
    main()
