Math =int(input("enter math marks"))
phy =int(input("enter phy marks"))
dbms =int(input("enter dbms marks"))
os =int(input("enter os marks"))
avg = (Math+phy+dbms+os)/4
if(avg>=75):
    print("Grade A")
elif(avg>=50):
    print("Grade B")
elif(avg>=30):
    print("Grade C" )
else:
    print("fail")


