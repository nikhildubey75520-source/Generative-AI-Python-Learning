'''ABSTRACTION :- Hiding the complexity and giving the function is known as abstraction 
example - atm machine , laptop, bike start stc....
There are two to achieve the concept of astarction 
1. abstract class
2. interface:-python can't support 
 
abstract class:- 
* a class is drived from ABC class which belongs to abc module is known as abstract class 
* we can't create object of abstract class 
* with the help of inheritance we can implement abstract class 
* it contains may or may not abstract method
* abstract method is a method which can't have any body
* we can declared constructor of abstract class 
* an abstract class can extend another abstract class  '''

# from abc import ABC,abstractmethod
# class Demo(ABC):
#     @abstractmethod  # predefined like save(),fetchALL(),findByID
#     def show():
#         pass
#     @abstractmethod
#     def msg():
#         pass
# class Test(Demo):
#     def show(self):
#         print("hello")
#     def msg (self):
#         print("hi")
# t=Test()
# t.show()
# t.msg()
# #d=Demo()
from abc import ABC,abstractmethod
class Test1(ABC):
    def __init__(self):
        self.a=10
        self.b=20
    @abstractmethod
    def show(self):
        pass
class Test2(Test1):
    def show(self):
        print(self.a)
        print(self.b)        
t=Test2()
t.show()


class Test1(ABC):
    @abstractmethod
    def m1():
        pass
class Test2(ABC):
    @abstractmethod
    def m2():
        pass
class Test3(Test1,Test2):
    def m1(self):
        print("hello")
    def m2(self):
        print("hi")
t=Test3()
t.m1()
t.m2()


