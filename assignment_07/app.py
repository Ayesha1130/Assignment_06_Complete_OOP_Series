#Access Modifiers: Public, Private, and Protected
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.


class Employee():
    def __init__(self,name,salary,ssn):
        self.name = name       # Public variable
        self._salary = salary # Protected variable (1 underscore)
        self.__ssn = ssn      # Private variable (2 underscore)

# Object created
emp = Employee("Ayesha", 100000, "123-456-789")

# Public variable: Access allowed
print("Name (Public) :",emp.name)

# Protected variable: Access technically allowed, lekin convention hai ke direct access na kiya jaye
print("Salary (_Protected) :",emp._salary)

# Private variable: Direct access not allowed, error aayega
try:
    print("SSN (__Private) :",emp.__ssn)
except AttributeError as e:
    print("Error Acessing Private Variable :",e)

# Lekin private variable ko indirectly access kiya ja sakta hai (name mangling ke zariye)
print("SSN (accessed via name mangling):", emp._Employee__ssn)