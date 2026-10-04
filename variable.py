# class Test:
#     #Class level variable
#     a=10
#     def __init__(self):
#         #instance variable
#         self.b=20
# t=Test()
# print(t.a,t.b)
# t.a=11
# t.b=22
# print(t.a,t.b)
# t1=Test()
# print(t1.a,t1.b)#a,b instance variables
#instance variables is varied from object to object

# class Demo:
#     def msg (self):
#         print("bye")
#     @classmethod
#     def show(cls):
#         print("hello")
#     @staticmethod
#     def display():
#         print("hi")
# d=Demo()
# #WE CAN ACCESS INSTANCE METHOD BY USING OBJECT REFERENCE 
# d.msg()
# #we can classmethod by using object reference as well as class name 
# Demo.show()
# d.show()
# #we can access staticmethod by using only class name 
# Demo.display()

# # WHEN USED INSTANCE , CLASSMETHOD, STATICMETHOD
# # SELF CAN GET OBJECT INFORNMATION 
# # CLS CAN GET CLASS INFORNMATION 
# # STATICMETHOD CAN GET ONLY LOGIC AND CALCULATION




# # WE CAN DECLARED STATIC/CLASS LEVEL VARIABLE INSIDE CLASS AND 
# # CONSTRUCTOR BUT BY USING CLASS NAME
# class Test:
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Test.count+=1
# t1=Test("Ravi")
# t2=Test("mukesh")
# t3=Test("rahul")
# print("number of employees " , Test.count)

# # diff b/w instance vs static/class vs local variable
# # instance variable - inside constructor
# # static  - inside class
# local variable - inside function

class Mine:
    mine_type = "Underground Mine"   # Class variable
    def __init__(self, name, gas, temperature):
        self.name = name              # Instance variable
        self.gas = gas                # Instance variable
        self.temperature = temperature # Instance variable
    def safety_status(self):
        status = "SAFE"               # Local variable
        if self.gas > 50:
            status = "DANGER"
        elif self.temperature > 45:
            status = "DANGER"
        return status
m1 = Mine("Coal Mine", 30, 35)

print("Mine Name:", m1.name)
print("Mine Type:", m1.mine_type)
print("Gas Level:", m1.gas)
print("Temperature:", m1.temperature)
print("Safety Status:", m1.safety_status())


