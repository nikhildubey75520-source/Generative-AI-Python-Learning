'''ERROR :- CAN'T HANDLE :- COMPILE TIME 
EXCEPTION HANDLING:- handle :-runtime 

why? 
example :- real life example :- ATM machine

developement -- coding :- manual coding ---copy&paste
100 lines of code hn
81 lines code :- we can get output
82 lines user mistakes
92---------------------
96---------------------
code ruuning mode

EXCEPTION HANDLING :- IS AN ABNORMAL CONDITION WHICH OCCURS AT RUN TIME .
THERE ARE THREE KEYWORDS TO HANDLE THE EXCEPTION 
1:- TRY 2:- EXCEPT 3:- FINALLY(OPTIONAL)


try:
//risky code(manual kr rhe hn ya toh copy and paste)
except:
    handling code

finally:
optional



'''

try:
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("exception generates")
finally:
    print("always executes")

# ab mujhe exception print krwana hn
# try:
#     a=int(input("enter first number"))
#     b=int(input("enter second number"))
#     c=a/b
#     print(c)
# # there is no statement between try and except
# except Exception as e:

#     print(e)
# finally:
#     print("always executes")


def vote():
    try:
        age=int(input("enter age"))
        if age<18:
            raise ValueError
        else:
            print("you are eligible for vote")
    except ValueError:
        print("you are not eligible for vote")
vote()


# how to implement banking app using abstract class and exception 
from abc import ABC, abstractmethod

class InsufficientException(Exception):
    pass


class BankAccount(ABC):

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amt):
        if amt <= 0:
            raise ValueError("Please enter a valid deposit amount")

        self.balance = self.balance + amt
        print("Amount deposited:", amt)
        print("After deposit balance is:", self.balance)

    @abstractmethod
    def withdraw(self, amt):
        pass

    def show_details(self):
        print("\n----- Account Details -----")
        print("Customer Name:", self.name)
        print("Account Number:", self.account_no)
        print("Your Balance is:", self.balance)


class Customer(BankAccount):

    def withdraw(self, amt):

        if amt <= 0:
            raise ValueError("Please enter a valid withdrawal amount")

        if amt > self.balance:
            raise InsufficientException(
                "Insufficient balance! Withdrawal cannot be completed."
            )

        self.balance = self.balance - amt

        print("Amount withdrawn:", amt)
        print("Remaining balance:", self.balance)


customer = Customer("Nikhil", 12345, 10000)

try:
    customer.show_details()

    customer.deposit(5000)

    customer.withdraw(3000)

    customer.withdraw(15000)

except InsufficientException as e:
    print("Error:", e)

except ValueError as e:
    print("Error:", e)