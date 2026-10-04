'''INHERITANCE :- THE PROCESS OF AQUIRING PROPERTIES AND BEHAVIOR FROM ONE TO ANOTHER CLASS IS KNOWN AS INHERITANCE
 THERE ARE FIVE TYPES OF INHERITANCE
 1)- SINGLE LEVEL INHERITANCE :- WHEN A CLASS INHERITS THE PROPERTIES OF ANOTHER IS KNOWN AS SINGLE
 2)- MULTILEVEL INHERITANCE :- WHEN A CLASS INHERITS THE PROPERTIES OF ANOTHER BUT THESE CLASS ALREADY INHERITED ANOTHER CLASS 
 3)- MULTIPLE INHERITANCE :- WHEN A CLASS INHERITS MORE THAN ONE CLASS
 4)- HIERARCHICAL INHERITANCE :- WHEN A CLASS INHERITED BY MORE THAN ONE CLASS
 5)- HYBRID INHERITANCE :- IT IS A COMBINATION OF HIERARCHICAL AND MULTIPLE INHERITANCE 
 '''

# single level inheritance
# class A:
#     def m1(self):
#         print("hello")
#     def m2(self,a,b):
#         print(a+b)
# class B(A):
#     pass
# b=B()
# b.m1()
# b.m2(2,4)

# multi level inheritance
class A:
    def m1(self):
        print("hi")
class B(A):
    def m2(self):
        print("bye")
class C(B):
    def m3(self):
        print("nikhil")
ob=C()
ob.m3()


'''baki aur v inheritance ka khud se example lekr aao'''

# multiple inheritance
class A:
    def m1(self):
        print("Class A")


class B:
    def m2(self):
        print("Class B")


class C(A, B):
    def m3(self):
        print("Class C")


ob = C()

ob.m1()
ob.m2()
ob.m3()

# hierarchial inheritance
class A:
    def m1(self):
        print("Class A")


class B(A):
    def m2(self):
        print("Class B")


class C(A):
    def m3(self):
        print("Class C")


ob1 = B()
ob2 = C()

ob1.m1()
ob1.m2()

ob2.m1()
ob2.m3()

# hybrid inheritance

class A:
    def m1(self):
        print("Class A")


class B(A):
    def m2(self):
        print("Class B")


class C(A):
    def m3(self):
        print("Class C")


class D(B, C):
    def m4(self):
        print("Class D")


ob = D()

ob.m1()
ob.m2()
ob.m3()
ob.m4()




