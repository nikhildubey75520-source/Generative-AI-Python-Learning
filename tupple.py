'''tupple are immutable means can't be changed or modified 
* are used to store heterogeneous 
* are used to store duplicates value 
* are used to declare paranthesis
* insertion order are preserved'''

t1=()
t2=(1,2,3,4)
t3=11,22,33
print(t3)
t4 = (11,22,[101,102])
t5 = ((1,2,3),("sun","mon","tue"))
print(t4)
print(t5)
t=(1,2,3,4,5,6,7,8)
'''count,index,remove,pop,sort,reverse,append,extend,insert,clear,copy'''
'''sum,max,min,len'''
t1=[1,2,3]
t2=[11,22,33]
t6=t1.append(t2)
t7=t1.append([101,102])
print(t2)
print(t1)
'''how to delete elements in tupple '''
n=(1,2,3,4)
tt= list(n)
tt.remove(2)
print(tt)


