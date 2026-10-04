'''Polymorphism :- is a greek word poly means many and morphism form when a action performed multiple operation in different ways is known as 
polymorphism 

THERE ARE TWO TYPES
1)- overloaded
2)- overriding

=> overloaded are three types

a)- operator overloading:- same operator but different operation

example- 10+20=30
"100" +"200" =100200
3*3 = 9       "ram"*3=ramramram

b)- method overloading:- python can't support 

c)- constructor overloading :- python can't support


2)- method overriding  => when parent class and child class having same method name but different logic is known as method overriding

Method overriding tab hota hai jab child class, parent class ke same method ko dobara define karti hai, lekin apne according uska behavior change kar deti hai.
'''
class Parent:
    def marry(self):
        print("west indies girl")
class Child(Parent):
    def marry(self):
        print("indian girls")
c=Child()
c.marry()


class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    class Address:
        def __init__(self,city,state):
            self.city=city
            self.state=state
        def show(self):
            print("City is",self.city)
            print("State is",self.state)
s=Student("rahul","java")
a=Student.Address("noida","up")
a.show()
print("name:",s.name)
print("Course:",s.course)



class ShoppingCart:
    class product:
        def __init__(self,name,price,quantity):
            self.name=name
            self.quantity=quantity
            self.price=price
        def total(self):
            return self.price*self.quantity
    def __init__(self):
        self.cart=[]
    def add_product(self):
        name=input("enter product name")
        price=int(input("enter product price"))
        quantity=int(input("enetr number of quantity"))

        p=self.product(name,price,quantity)
        self.cart.append(p)
        print("product Added Successfully")
    def show_cart(self):
        for c in self.cart:
            print(c.name,c.price,c.quantity,c.total())
shop =ShoppingCart()
shop.add_product()
shop.show_cart()

'''| Code                                 | Concept                            |
| ------------------------------------ | ---------------------------------- |
| `Parent → Child` with same `marry()` | **Method Overriding**              |
| `Student` containing `Address`       | **Nested Class**                   |
| `ShoppingCart` containing `Product`  | **Nested Class + Object Creation** |
| `super().marry()`                    | **Calling Parent Method**          |
| `self.cart = []`                     | **List as Instance Variable**      |
| `p.total()`                          | **Calling Object Method**          |
'''





