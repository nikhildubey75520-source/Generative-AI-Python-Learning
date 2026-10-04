# '''dictionary :- are used to store key-value pair where key are unique and values may be duplicate 
# * dictionary are mutable
# * insertion order preserved 
# * slicing are not possible 
# '''
# d1=dict()
# print(type(d1))


# d={
#     "id":1,
#     "name":"bitu",
#     "course":"python",
#     "age":23,
#     "city":"delhi"

# }
# print(d)


# keys=[1,2,3,4]
# values=["bitu","nikhil","kishlay","hamza"]
# d=dict(zip(keys,values))

# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# print(tuple(d.items()))
# '''big bracket hatane k liye tuple me convert karna padta hai'''

# k=["id","name","course","age","city"]
# v=[1,"bitu","python",23,"delhi"]
# d=dict(zip(k,v))
# print(d)
# print(d.get("name"))

# d={
#     "id":1,
#     "name":"bitu",

# }
# print(d)
# ''' * update the value of key
# * remove the key value pair'''
# d.update({"name":"nikhil"})
# print(d)
# d.pop("name")
# print(d)


'''implementation of dictionary in minor project'''
employee=dict()
while True:
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice==1:
        name=input("enter employee name:")
        department=input("enter employee department:")
        id=int(input("enter employee id:"))
        age=int(input("enter employee age:"))
        employee[id]={
            
            "name":name,
            "department":department,
            "id":id,
            "age":age
        }

        print("employee added successfully")

    elif choice==2:
        if len(employee)==0:
            print("no employee found")
        else:   
            for id in employee:
                emp = employee[id]
                print("name:\n",emp["name"])
                print("department:\n",emp["department"])
                print("id:\n",emp["id"])
                print("age:\n",emp["age"])
    elif choice==3:
        search_name=input("enter employee name to search:")
        found = False
        for id in employee:
            emp = employee[id]
            if emp["name"] == search_name:
                print("name:\n",emp["name"])
                print("department:\n",emp["department"])
                print("id:\n",emp["id"])
                print("age:\n",emp["age"])
                found = True
        if not found:
            print("employee not found")
    elif choice==4:
        search_id=int(input("enter employee id to update:"))
        if search_id in employee:
            emp = employee[search_id]
            print("Current details:")
            print("name:\n",emp["name"])
            print("department:\n",emp["department"])
            print("id:\n",emp["id"])
            print("age:\n",emp["age"])
            
            name=input("enter new employee name:")
            department=input("enter new employee department:")
            age=int(input("enter new employee age:"))
            
            emp["name"] = name
            emp["department"] = department
            emp["age"] = age
            
            print("employee updated successfully")  
    elif choice==5:
        delete_name=input("enter employee name to delete:")
        if delete_name==name:
            name=""
            department=""
            id=0
            age=0
            print("employee deleted successfully")
        else:
            print("employee not found")
    elif choice==6:
        print("exit")
        break
    else:
        print("invalid choice")
        







