#Static Variables and Static Methods
#Create a class MathUtils with a static method add(a, b) that returns the sum. 
# No class or instance variables should be used.

class MathUtils():

    # Static method: yeh class ya object par depend nahi karta
    @staticmethod
    def add(a,b):
        return a + b # Dono numbers ka sum return karega
    

 # Static method ko class ke zariye call karte hain (object banane ki zarurat nahi) 
result = MathUtils.add(10,30)
print("Sum is : ",result)

        

