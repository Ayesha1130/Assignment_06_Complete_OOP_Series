# Aggregation
# Create a class Department and a class Employee. Use aggregation by having a Department 
# object store a reference to an Employee object that exists independently of it.

class Employee():
    def __init__(self,name):
        self.name = name  # Employee ka naam set kar rahe hain


class Department:
    def __init__(self,dept_name,employee):
        self.dept_name = dept_name
        self.employee = employee

    def show_info(self):

        print(f"Department : {self.dept_name}")
        print(f"Employee {self.employee.name}")

# Pehle Employee object banaya (ye independent hai)
emp1 = Employee("Ayesha")


# Phir Department object banaya, jismein employee ka reference diya
dept1 = Department("HR",emp1)

# Department ka info show kar rahe hain
dept1.show_info()