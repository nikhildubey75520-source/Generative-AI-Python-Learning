class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def grade(self):
        if self.marks>=90 :
            print("A+")
        elif self.marks>=75 and self.marks<=90:
            print("B+")
        elif self.marks>=50 and self.marks<=75:
            print("C+")
        elif self.marks>=35 and self.marks<=50:
            print("fail")
student=dict()
while True:
    print("1.Add")
    print("2.view")
    print("3.search")
    print("4.update")
    print("5.delete")
    print("6.exit")

    ch=int(input("enter your choice:"))
    if ch==1:
        roll=int(input("enter roll number:"))
        name=input("enter student name:")
        marks=int(input("enter marks:"))
        s=Student(name,marks)
        student[roll]=[s.name,s.marks,s.grade()]
        print(student)
    elif ch==2:
        print(student)
    elif ch==3:
        print("enter roll number of student:")
        roll=int(input())
        if roll in student:
            print("student[roll]")
        else:
            print("Student not found")
    elif ch==4:
        print("enter roll number of student to update:")
        roll=int(input())
        if roll in student:
            marks=int(input("enter new maarks:"))
            s=Student(student[roll][0],marks)
            student[roll][1]=s.marks
            student[roll][2]=s.grade()
            print("marks and grade updated successfully")
        else:
            print("Student not found")
    elif ch==5:
        print("enter roll number of student to delete: ")
        roll=int(input())
        if roll in student:
            del student[roll]
            print("Student deleted successfully")
        else:
            print("Student not found")
    elif ch==6:
        print("exited!")
        break
    else:
        print("invalid choice")

        
