# Class Decorators
# Create a class decorator add_greeting that modifies a class to add a greet()
# method returning "Hello from Decorator!". Apply it to a class Person.

# Class decorator define kiya
def add_greeting(cls):
    # greet method define kar rahe hain jo object ka naam use hoag
    def greet(self):
        return f"Hello, {self.name}! Greeting from Decorator."
    
    cls.greet = greet  # greet method class mein attach kiya
    return cls  # Modified class return kiya

# Person class par decorator apply kiya
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name  # Har person ka naam set kiya

# Object create kiya
p1 = Person("Ayesha")
p2 = Person("Sara")

# Personalized greeting call ki
print(p1.greet())  # Output: Hello, Ali! Greeting from Decorator.
print(p2.greet())  # Output: Hello, Sara! Greeting from Decorator.



