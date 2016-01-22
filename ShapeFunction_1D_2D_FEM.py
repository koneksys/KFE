"""Created on Thu Aug 13 12:26:26 2015
//Generating Shape_Functions
@author: Jerome Szarazi, Koneksys
if the package required are not available look up with the command 
import sys and sys.path the directory where the libraries are installed.
download the missing file and copy it to the directory
"""
from sympy import*
from sympy.abc import alpha
from sympy.polys.monomials import itermonomials
from scipy.special import comb


Specification = {'Quantity_type':'vector','Topology':{'Polytope':'Simplex','Dim':2 },'1Face': {'FD':1,'PE':1,'NC':1},'0Face': {'FD':1,'PE':1,'NC':1}}
"""It give the index for set comparison"""
RefSpecInfo=['Quantity_type','Topology','0Face','1Face','2Face','3Face']
RefQuantityType=['Scalar','Vector','PseudoScalar','PseudoVector']
FaceReqType=['PE','FD','SD','ND','TC','NC','DD','IM']
"""We have the element in the set which is correspond to the specification"""
"""We would have to look for the type of specification and then
count at each dimensional space the number of requirement types"""
index=0
FacesSpec=[]
for j in range(0,len(Specification)):
          if RefSpecInfo[1]==Specification.items()[j][0]:
                index=j 
                TS=Specification.items()[index]
                PolytopeType=(TS[1].items()[1])[1]
                Dim=(TS[1].items()[0])[1]
                del index
          elif RefSpecInfo[0]==Specification.items()[j][0]:
                index=j
                Quantity_type=(Specification.items()[index])[1]
                del index
          else:
                FacesSpec.insert(0,Specification.items()[j])
                
"""defining an array ////from numpy import numarray///
FaceSpecArray = array([ [0] * 4 ] * 7) package refers to numpy"""

from numpy import array
FaceSpecArray = array([ [0] * 7 ] * 4)

    """READING FUNCTIONAL SPECIFICATION - STORING INFORMATION in ARRAY"""
"""FacesSpecArray: Array where functional information associated to m-faces are stored
The row are the m-face and the columns follows of FaceReqType array
FacesSpec: it contains all set of information of faces (Specification information except Polytope&Dim information)
FaceDim=Read the first character of mface to find dimension of mface
FaceDef=Read functional information of an mface"""

for i in range(0,len(FacesSpec)):
    for j in range(0,len(FacesSpec[i])):
        FaceDim= int(FacesSpec[i][0][0])
        for k in range(0,len(FacesSpec[i][1])):
            FaceDef=FacesSpec[i][1]
            for n in range(0,len(FaceDef)):
                if FaceDef.items()[n][0]=='PE':
                    FaceSpecArray[FaceDim,0]=FaceDef.items()[n][1]
                elif FaceDef.items()[n][0]=='FD':
                    FaceSpecArray[FaceDim,1]=FaceDef.items()[n][1]
                elif FaceDef.items()[n][0]=='SD':
                    FaceSpecArray[FaceDim,2]=FaceDef.items()[n][1]
                elif FaceDef.items()[n][0]=='ND':
                    FaceSpecArray[FaceDim,3]=FaceDef.items()[n][1]
                elif FaceDef.items()[n][0]=='TC':
                    FaceSpecArray[FaceDim,4]=FaceDef.items()[n][1]
                elif FaceDef.items()[n][0]=='NC':
                    FaceSpecArray[FaceDim,5]=FaceDef.items()[n][1]
                elif FaceDef.items()[n][0]=='DD':
                    FaceSpecArray[FaceDim,6]=FaceDef.items()[n][1]
                elif FaceDef.items()[n][0]=='IM':
                    FaceSpecArray[FaceDim,7]=FaceDef.items()[n][1]

    """CALCULATION OF THE TOPOLOGICAL COMPONENTS"""
"""we have the dimension and the type of Polytope, we can therefore calculated
the composition of the polytope"""
Face=[]
if (PolytopeType == 'Simplex'): 
    for i in range(0,(FaceSpecArray.shape)[0]): Face.insert(i,comb(Dim+1,i+1))       
if (PolytopeType == 'Cube'): 
    for i in range(0,(FaceSpecArray.shape)[0]): Face.insert(i,pow(factorial(i)*factorial(Dim-i),-1)*factorial(Dim)*pow(2,Dim-i))      
 
"""We have to evaluate the functional space based upon the functional specification
of the m-face"""

                """DOF CALCULATION"""
"""Size of the specification array is provided by python method ".shape"; the first
element is the space dimension: point, line, surface, volume thus length
is equal to 4...which should'nt change except we are considering space-time problem."""
SizeFaceSpec=(FaceSpecArray.shape)[1]

NbDOF=0
if Dim==1:
    for i in range(0,SizeFaceSpec+1):
        NbDOF=sum(FaceSpecArray[i]*Face[i])
if Dim==2 & Quantity_type==RefQuantityType[0]:
    NbDOF=sum(FaceSpecArray[0]*2)+sum(FaceSpecArray[1])
if Dim==2 & Quantity_type==RefQuantityType[1]:
        
"""Calculation of the polynomial"""
x,y,z=symbols('x y z')
from sympy.abc import alpha

if Dim==1: 
    PB=itermonomials([x], NbDOF-1)
elif Dim==2:
    PB=itermonomials([x, y], NbDOF-1)
elif Dim==3: 
    PB=itermonomials([x, y, z], NbDOF-1)

"""Representation of the polynomial"""
PBL=list(PB)
A = MatrixSymbol('alpha', 1, NbDOF)
ALPHA=Matrix(A)
P=Matrix(A)*Matrix(PBL)
"""Analytical representation of functional evaluation"""
"""Point Evaluation - PE"""
PE=P[0]
"""First derivative evaluation -FD"""
FD=diff(PE,x,1)
"""At this stage all the coordinate information of the vertice should
be calculated in order to evaluate the DOF"""
"""Definition coordinate vertice"""
from sympy import Rational


if Dim==1:
    NbNode=max(FaceSpecArray[1])+2
    NodeCo=[]; PE_N = []; FD_N = []; CoefMatrix= array([ [0] * NbDOF ] * NbDOF)
for i in range(0,NbNode): 
    NodeCo.insert(i,Rational(2*i,NbNode-1)-1)
    PE_N.insert(i,PE.subs(x,NodeCo[i]))
    FD_N.insert(i,FD.subs(x,NodeCo[i]))

from sympy.matrices import zeros
CoefMatrix=zeros(NbDOF,NbDOF)
for i in range(0,len(PE_N)):
    PE_Ni=PE_N[i].as_coefficients_dict()
    for n in range(0,len(PE_Ni)):
        ReadCoefNamePE=PE_Ni.items()[n][0]       
        ReadCoefValuePE=PE_Ni.items()[n][1]
        for k in range(0,NbDOF):
            if ALPHA[k] == ReadCoefNamePE: CoefMatrix[i,k]=ReadCoefValuePE

for i in range(0,len(FD_N)):
    FD_Ni=FD_N[i].as_coefficients_dict()
    for n in range(0,len(FD_Ni)):
        ReadCoefNameFD=FD_Ni.items()[n][0]       
        ReadCoefValueFD=FD_Ni.items()[n][1]
        for k in range(0,NbDOF):
           if ALPHA[k] == ReadCoefNameFD: CoefMatrix[i+len(PE_N),k]=ReadCoefValueFD


"""Calculate the Shape function"""
ShapeMatrix=zeros(NbDOF,1)

ShapeList=[]
for i in range(0,NbDOF):
    ShapeList.insert(i,(CoefMatrix.inv())[:,i].transpose()*Matrix(PBL))
"""Problem of Latex reading the array, have to read just one element"""
x = np.arange(-0.5, 0.5, 0.01)  
s = ShapeList[1]
              
from IPython.display import Image, display
from IPython.lib.latextools import latex_to_png


eq = r'F(k) = \int_{-\infty}^{\infty} f(x) e^{2\pi i k} dx'
data = latex_to_png(latex(ShapeList[1]), wrap=True)
display(Image(data=data))
with open('picture_out.png', 'wb') as f:
    f.write(data)

from sympy import symbols
from sympy.plotting import plot

x = symbols('x')
p = plot(x)

plot(x, x**2, x, (x, -1, 1),hold='true')

x = N . arange ( -1 , 1 , 0.01)
s=(x,ShapeList[0][0])
values=s[0]
pylab . plot (x , values )


srepr(ShapeList[0][0])

p=plot(ShapeList[0][0],ShapeList[1][0],ShapeList[2][0], (x, -1, 1));
p1=plot(ShapeList[3][0], (x, -1, 1))

p.append(p1[0])
p=plot(ShapeList[0][0],ShapeList[1][0],ShapeList[2][0],ShapeList[3][0], (x, -1, 1))

p=plot(ShapeList[0][0],ShapeList[1][0],ShapeList[2][0],ShapeList[3][0],ShapeList[4][0],ShapeList[5][0], (x, -1, 1))

"""Calculating the stifness matrix of a beam"""

del DB_SD,BL_SD,p,Ke
ShapeListSD=[]
KeL=[]
Ke=Matrix(KeL)

Ke=zeros(NbDOF,NbDOF)
"""Ke = array([ [0] * NbDOF ] * NbDOF)"""
for i in range(0,NbDOF):
    ShapeListSD.insert(i,diff(ShapeList[i][0],x,1))
DB_SD=Matrix(ShapeListSD)
BL_SD=DB_SD*DB_SD.transpose()
for i in range(0,NbDOF):
    for j in range(0,NbDOF):
        p=Poly(BL_SD[i,j],x)
        PI=p.integrate(x)
        Ke[i,j]=PI(1)-PI(-1)
        
PI=p.integrate(x)
I11=PI(1)-PI(-1)


