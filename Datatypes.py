''' int,float,boolean,str,list,dictioinary,set,complex,none,byte,bytearray,range,tuple'''

'''set: unordered collection of unique elements'''
'''dictionary: unordered collection of key-value pairs'''
'''tuple: ordered collection of elements, immutable'''
'''list: ordered collection of elements, mutable'''
'''boolean: True or False'''
'''complex: complex numbers with real and imaginary parts'''
'''none: represents the absence of a value or a null value'''
'''byte: immutable sequence of bytes'''
'''bytearray: mutable sequence of bytes'''
'''range: represents a sequence of numbers, commonly used in loops'''
'''str: ordered collection of characters, immutable'''
'''float: represents decimal numbers'''
'''int: represents whole numbers, both positive and negative'''
'''there are some mutable datatypes and immuatable dtatypes in python, mutable datatypes can be changed after creation, while immutable datatypes cannot be changed after creation.'''
'''list are mutable datatypes and which is used to create dynamic array , are heterogeneous , are used to store index basis , duplicates allowed , none value are allowed , and used to decleared []'''


'''many ways to create list'''
t1=[]
print(t1)
print(type(t1))
t2=[1,2,3,4]
t3=[11,22,[101,102,103]]
t4=[111,"ram",'t',23.5,111]
t5="techlive"
t6=list(t5)
t7="techlive solution pvt ltd"
t8=t7.split()

t9=input("enter elements")
t10=list(map(int,input("enter elements").split()))
print(t10)
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)
print(t9)
t=[]
for i in range (1, 6):
    n=list(map(int,input("enter elements").split()))
    t.append(n)
print(t) 