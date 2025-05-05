#Abstract Classes and Methods
#Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().

# abc module se abstract base class ka support liya
from abc import ABC, abstractmethod

# Shape aik abstract class hai
class Shape(ABC):
    @abstractmethod

    def area(self): 
        pass  # Ye method sirf declare kiya, implement nahi kiya

# Rectangle class, Shape class se inherit karti hai
class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
       return self.width * self.height # Area calculate kar ke return kar rahe hain

 # Rectangle ka object banaya jismein width 5 aur height 4 hai
rect = Rectangle(5,4)
print("Area of Rectangle",rect.area())

        

