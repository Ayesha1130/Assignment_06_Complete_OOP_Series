# The super() Function
# Create a class Person with a constructor that sets the name. Inherit a class Teacher
#  from it, add a subject field, and use super() to call the base class constructor.

# Person aik base (parent) class
class Person():
    def __init__(self,name):
        self.name = name

# Teacher class, Person class se inherit kiya
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name) # Parent class (Person) ka constructor call ki
        self.subject = subject

#create object
teacher1 = Teacher("Miss Ayesha","English")

# Object ke attributes ko print kar rahe hain
print("Name :", teacher1.name)
print("Subject :", teacher1.subject)
    

