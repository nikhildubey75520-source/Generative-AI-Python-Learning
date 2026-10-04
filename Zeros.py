# is used to availability like product ,loan,email
# 0 and 1 is mostly used in binary classification
# import numpy as np
# o=np.ones(4)
# print(o)
# o2=np.ones((4,4))
# print(o2)
# o3=np.ones((3,3,3))
# print(o3)

# WHY SLICING OR INDEXING IN NUMPY ?

# indexing in 1D
# a1=np.array([1,2,3,4,5,6,7,8,9])
# print(a1[0])

# indixing in 2D

# a2=np.array([[1,2,3,4],[5,6,7,8]])
# print(a2[0][1])

# indexing in 3D 3,5,7,4,5,6
# a3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(a3[2][1][0])
# print(a3[0][1][2])



# slicing in 1D
# a1=np.array([1,2,3,4,5,6,7,8,9])
# print(a1[0:])

# slicing in 2D
# a2=np.array([[1,2,3,4],[5,6,7,8]])
# print()

# SHAPE AND RESHAPE
# a1=np.array([1,2,3,4,5])
# print(a1.shape)
# a2=np.array([1,2,3,4,5,6,7,8,9])
# print(a2.shape)
# s= a2.reshape(3,3)
# print(s)

# import numpy as np
# x=np.arange(1,9)
# #  (2,2,2) eska mtlb ye hn ki kitna row kitna column aur kitna dimension ka matrix bnega 
# y=x.reshape(2,2,2) 
# print(y)
# print(y.ndim)

# next is age and salary ,bonous,gross,net salary
# in product , if purchase 10000 then free delivery
# in product if purchase 5000 then 5% discount 
# is used for(inc or dec)
# a=np.array([1,2,3,4,5,6])
# x=a+2
# y=a*2
# print(x)
# print(y)

# a1=np.array([[1,2,3,4],[5,6,7,8]])
# a2=np.array([11,22,33,44])
# z1=a1+a2
# z2=a1*a2
# z3=a1/a2
# print(z1)
# print(z2)
# print(z3)


# n=np.array([1,2,3,4,5,6,7,8,9])
# print(np.sum(n))
# print(np.size(n))
# print(np.max(n))
# print(np.min(n))
# print(np.mean(n))
# print(np.median(n))

# WHY MEAN AND MEDIAN USED IN ML ?
# QUESTION HOMEWORK

# n=np.array([10,20,30,40,50])
# print(np.cumsum(n))
# print(np.cumprod(n))
# import numpy as np
# t=np.array([[1,2],[4,5]])
# print(np.cumprod(t))
# print(np.cumsum(t))

# n=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(np.array(np.cumsum(n)))
# print(np.array(np.cumprod(n)))


# n=np.array([[10,20,30],[40,50,60]])
# print(n)
# print(np.sum(n,axis=0))
# print(np.sum(n,axis=1))


# n=np.array([[[10,20,30],[40,50,60],[30,70,90]]])
# print(n)
# print(np.sum(n,axis=0))
# print(np.sum(n,axis=1))
# print(np.sum(n,axis=2))

'''8th interview question 
=>mean and median are used to fill blank value in ML 
=> axis =0, axis=1 is used to calculate vertically and horizontally and axis =1 is mostly used in ml for drop dependent variable/target variable for ml training purpose
'''

'''pandas is used for perform operation on dataset 
there are two types
1=> series(1-D)  2=> dataframe (2-D)
'''

# import pandas as pd
# import numpy as np
# s1=pd.Series()
# print(s1)
# s2=np.array([1,2,3,4,5])
# s3=pd.Series(s2)
# print(s3)
# s4=pd.Series([11,22,33,44])
# print(s4)

# s5=pd.Series(["aman","chaman","sonu","monu"],index=["A","B","C","D"])
# print(s5)

# shape and dtype are important for ML
# import pandas as pd
# s6=pd.Series([[10,20,30,40,50],[2,3,4,5,6]])
# print(s6.index)
# print(s6.shape)
# print(s6.size)
# print(s6.values)
# print(s6.dtype)

# data=[
#     [1,"david","developer",23000,"noida"],
#     [2,"pitter","programmer",45000,"delhi"],
#     [3,"kumar","hr",32000,"bangalore"],
#     [4,"sahil","trainee",16000,"chennai"],
#     [5,"hari","manager",50000,"delhi"]

# ]
# df=pd.DataFrame(data)
# print(df)
# import pandas as pd
# data=[
#     [1,"david","developer",23000,"noida"],
#     [2,"pitter","programmer",45000,"delhi"],
#     [3,"kumar","hr",32000,"bangalore"],
#     [4,"sahil","trainee",16000,"chennai"],
#     [5,"hari","manager",50000,"delhi"]

# ]

# df=pd.DataFrame(data,columns=["Id","Name","Post","Salary,"City" ])
# print(df) 

# # 2nd way 2D Dataset
# import pandas as pd
# emp={
#     "id":[1,2,3],
#     "name":["nikhil","bitu","annu"],
#     "age":[20,21,20],
#     "marks":[85,95,75]

# }
# df=pd.DataFrame(emp)
# print(df)


# import pandas as pd
# emp={
#     "id":[1,2,3],
#     "name":["nikhil","bitu","annu"],
#     "age":[20,21,20],
#     "marks":[85,95,75]

# }
# df=pd.DataFrame(emp)
# df.head()
# print(df.head(1))


import pandas as pd
emp={
    "id":[1,2,3],
    "name":["nikhil","bitu","annu"],
    "age":[20,21,20],
    "marks":[85,95,75]

}
df=pd.DataFrame(emp)
df.tail()
print(df.tail(1))






'''Data Analyst-----Excel
ML---AI-------- Excel data
real time problrem '''


                              











