'''IN PYTHON , EACH AND EVERY ARE OBJECTS
WHAT IS OBJECT ?
OBJECT IS A REAL WORLD ENTITY WHICH CONSISTS STATE AND BEHAVIOR 
EXAMPLE - PEN IS AN OBJECT
1 PEN NAME COLOUR DESIGN REPRESENT VALUE OF AN OBJECT (STATE)(PEOPLE SELCT THIS OPTION)
1 PEN XXXXXXXXXXXXXXXX (NOT THIS)
BEHAVIOR REPRESENT WRITING SOME
OBJECT IS AN INSTANCE OF CLASS MEANS 
* OBJECT IS A MEMORY LOCATION WHICH IS USED TO STORE DATA TEMPORARY
(EXAMPLE-THE PLACE WHERE I SIT CURRENTLY IS TEMPERORARY)
* -> OBJECT CONTAINS PROPERTIES(VARIABLES) AND BEHAVIOR(FUNCTION/METHOD)
        ROLL,NAME,BRANCH,------PROPERTIES (VARIABLE)
        BEHAVIOR REPRESENT FUNCTIONALITY OF AN OBJECT
        DANCE(),WALK(), IS A FUNCTION-----def fun()

        
        
*-> CLASS IS BLUEPRINT/TEMPLATES
*-> CLASS IS A LOGICAL THING OR BLUEPRINT BUT NOT PHYSICALLY EXIST'''


''''class Test:
        logic implement 
flower 
rose,lotus is an object of class flower furniture 
chair , table is an object of class furniture


* class is a collection of objects

=> HOW TO CREATE ? 
'''
# class Test:
#     def __init__(self):
#         print("hello")
# t = Test()    #(is a constructor , which is used to initialize of an object )(self and t jo hn wo reference variable hn)



# class Test:
#     def __init__(self):
#         print(id(self))
# t=Test()
# print(id(t))

'''variable :- is a memory location which is used to store data 
there are three type of variable
1)- instance variable(object level)
2)- static variable(class level variable)
3)- class level variable
Method :-are used to write business logic (own logic)
there are three types
1)- instance method
2)- static method
3)- class method


1)-- instance variables is a variable which are decleared inside constructor , method are also outside of a class 

*)- with the help of reference variable we can access instance variable 

1)-- instance method :- is a method can accesss instance variable static variable and class level variable
CONSTRUCTOR - is used to initialization of an object and constructor can executes automatically at the time of object creation 
There are two types
1)-- default constructor :- no arguments
2)-- parametrized constructor
Note:-we can decleared only one constructor inside a class 

  '''

# class Test:
#     def __init__(self):
#         #instance variable
#         self.a=10
#         self.b=20
# t=Test()
# print(t.a)
# print(t.__dict__)#is a keyword which is used to access class attributes 


# class Test():
#     def __init__(self):
#         # instance variable
#         self.a=10
#         self.b=20
#         # instance method can access instance variable
#     def add(self):
#             print(self.a+self.b)
# t=Test()
# t.add()


# class user:
#     def __init__(self,name,password):
#         self.name=name
#         self.password=password
#     def login(self):
#         if self.name=='Techlive' and self.password ==123:
#             print("valid user")
#         else:
#             print("Invalid user")
# name = input("enter name")
# password= int(input("enter password"))
# u=user(name,password)
# u.login()

# Real Time Application using class and object

class customer:
    bname ="HDFC Bank Mohali"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("After Deposit Balance is",self.balance)
    def withdraw(self,amt):
        if self.balance <amt:
            print("insufficient balance")
        self.balance=self.balance-amt
        print("After Withdraw Balance is ", self.balance)
name=input("enter customer name")
c=customer(name)
print("welcome to",customer.bname,"Mr. ",name)
while True:
    print("d-Deposit")
    print("w-withdraw")
    print("e-Exit")
    ch=input("enter your choice ")
    if ch=='d' or ch=='w':
        amt=int(input("enter amount for deposite"))
        c.deposit(amt)
    elif ch=='w' or ch=='w':
        amt=int(input("enter amout to withdraw"))
        c.withdraw(amt)
    elif ch=='e' or ch=='E':
        print("Thank for using HDFC ATM Mohali")
        break
    else:
        print("invalid choice")




     



