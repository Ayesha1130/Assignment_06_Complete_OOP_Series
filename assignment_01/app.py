#  1. Using self
#  Create a class Student with attributes name and marks. Use the self keyword to
#  initialize these values via a constructor. Add a method display() that prints
#  student details.

class Student():
    def __init__(self,name,marks):
        self.name = name   # initializing name
        self.marks = marks   # initializing marks

    def display(self):
        print("Student Name :" , self.name)
        print("Student Marks :", self.marks)

student1 = Student("Ali",95)
student1.display()

student2 = Student("Ayesha", 100)
student2.display()

        

