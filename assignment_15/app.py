# Method Resolution Order (MRO) and Diamond Inheritance
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
#Create an object of D and call show() to observe MRO.



# Class A define ki (top of diamond)
class A:
    def show(self):
        print("Show method in class A")

# Class B, class A se inherit kar rahi hai
class B(A):
    def show(self):
        print("Show method in class B")

# Class C bhi class A se inherit kar rahi hai
class C(A):
    def show(self):
        print("Show method in class C")

# Class D, B aur C dono se inherit kar rahi hai (Diamond bana)
class D(B, C):
    pass  # Is class mein kuch override nahi kar rahe

# Object create kar rahe hain class D ka
d = D()

# show() method call kar rahe hain — MRO ke mutabiq decide hoga kaun sa method chalega
d.show()
