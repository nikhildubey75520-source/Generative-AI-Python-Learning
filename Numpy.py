# NUMPY IS USED FOR MATHEMATICAL CALCULATION FOR ML ,DL AND AI 
# WHY NUMPY ? 
# => EASY COMPLEX PROBLEM
# => EFFICIENT CODE
# => ARE USED TO STORE n-dimensional
# => performs indexed operation 
# => is used EDA(Exploratory Data Analysis) for ML, DL, AND AI
# HAMARA JO MACHINE HN USKO TRAIN KRNE K LIYE HMLOG USED KRTE HN NUMPY KA AUR ESKO HMM EDA V BOLTE HN
#  import numpy as np
# n1=np.array([1,2,3,4,5])   
# print(n1)
# print(n1.size)
# print(type(n1))
# print(n1.ndim)
# #  MODEL ALWAYS ACCEPT 2D ARRAY
# n2=np.array([[1,2,3,4],[5,6,7,8]])
# print(n2)
# print(n2.size)
# print(type(n2))
# print(n2.ndim)

# n3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(n3)
# print(n3.size)
# print(type(n3))
# print(n3.ndim)
# # IN CASE YOU USE 3D ARRAY THEN MUST BE CONVERTED INTO 2D ARRAY THEN MODEL TRAINED

# n4=np.array([[[[1,2,3],[4,5,6],[7,8,9],[1,9,8]]]])
# print(n4)
# print(n4.size)
# print(type(n4))
# print(n4.ndim)

# BUT ML ME HMM 4D ARRAY USE NI KR SKTE .



# n=int(input("enter number of elements"))
# n5=np.array(list(map(int,input("enter elements").split())))
# print(n5)
import numpy as np
rows=int(input("enter number of rows"))
cols=int(input("enter no of cols"))

t=[]
for i in range(rows):
    row=[]
    for j in range(cols):
      n6=int(input("enter elements"))
      v=list(map(int,input().split()))
      row.append(v)
    t.append(v)
n6=np.array(t)
print(n6)







