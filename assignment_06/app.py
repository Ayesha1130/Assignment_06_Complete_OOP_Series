# 6. Constructors and Destructors
# Create a class Logger that prints a message when an object is created (constructor)
#  and another message when it is destroyed (destructor).

class Logger():
     
       # Constructor: Jab object banega, yeh method chalega
     def __init__(self):
          print(" Logger Object Created")

    # Destructor: Jab object delete hoga ya program end hoga, yeh method chalega
     def __del__(self):
          print("Logger Object Destroyed")

# Example Usage
log = Logger()  # Object create kiya -> constructor chalega

# Optional: Manually destroy the object (agar foran destructor dekhna ho)
del log
     
        

