'''a piece of code that slices a list into smaller lists of a specified size.
a b c d e f g h i j k l m 
0 1 2 3 4 5 6 7 8 9 10 11 12

syntax:[start:end:stop]
*start optional but deafult value 0
end optional but by default value end -1 or length of list
stop optional but by default value 1'''
'''l1 = [1,2,3,4,5,6,7,8,9,10]
even =[]
for i in range (1,len(l1),2):
    even.append(l1[i])
print(even)'''
t = [1,2,4,6,2,5,2,8,9,2]
'''with the help of pop function we can remove the element from the list and it will return the removed element but index is optional if we don't provide the index then it will remove the last element from the list'''

t.pop(2)
print(t)

'''interview based'''
t=[1,2,3,4,5,6,7,8,9,10]
print(sum(t))
print(sum(t)/len(t))

'''minor project using list'''
'''students=[]
while True:
    print("1. Add Student")
    print("2. view Student")
    print("3. search student")
    print("4. find max marks with name ")
    print("5: exit")
    ch =int(input("Enter your choice: "))
    if ch == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        students.append([name,marks])
        print("Student added successfully!")
    elif ch == 2:
        print("Student List:")
        for student in students:
            print("Name:", student[0], "Marks:", student[1])
    elif ch == 3:
        search_name = input("Enter student name to search: ")
        found = False
        for student in students:
            if student[0] == search_name:
                print("Name:", student[0], "Marks:", student[1])
                found = True
                break
        if not found:
            print("Student not found.") 
    elif ch == 4:
        if students:
            max_student = max(students, key=lambda x: x[1])
            print("Student with maximum marks:")
            print("Name:", max_student[0], "Marks:", max_student[1])
        else:
            print("No students available.")
    elif ch == 5:
        print("Exiting the program.")
        break'''
'''enter product name
    enter quantity
    enter price
    1). add product
    2). view product with price

    3). gst calculate
    4). discount >=3000 10% , <=2000 6%
    5). final bill'''

product=[]
while True:
    print("1. Add Product")
    print("2. View Products with Price")
    print("3. Calculate GST")
    print("4. Apply Discount")
    print("5. Final Bill")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        product.append([name, quantity, price])
        print("Product added successfully!")
    
    elif choice == 2:
        print("Product List:")
        for item in product:
            print(f"Name: {item[0]}, Quantity: {item[1]}, Price: {item[2]}")
    
    elif choice == 3:
        gst_rate = 0.18  # Assuming GST is 18%
        total_gst = sum(item[1] * item[2] * gst_rate for item in product)
        print(f"Total GST: {total_gst}")
    
    elif choice == 4:
        total_amount = sum(item[1] * item[2] for item in product)
        if total_amount >= 3000:
            discount = total_amount * 0.10
        elif total_amount <= 2000:
            discount = total_amount * 0.06
        else:
            discount = 0
        print(f"Discount Applied: {discount}")
    
    elif choice == 5:
        total_amount = sum(item[1] * item[2] for item in product)
        gst_amount = total_amount * 0.18
        final_bill = total_amount + gst_amount
        if total_amount >= 3000:
            final_bill -= total_amount * 0.10
        elif total_amount <= 2000:
            final_bill -= total_amount * 0.06
        print(f"Final Bill Amount: {final_bill}")
    
    elif choice == 6:
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice! Please try again.")


