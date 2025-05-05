# 2. Using cls
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.

class Counter():
    count = 0  # Yeh ek class variable hai jo objects ki total count rakhta hai

    def __init__(self):
        # Har bar jab naya object banega, count mein 1 add hoga
        Counter.count += 1

      # Yeh ek class method hai, jo class variable ko access karke count show karta hai
    @classmethod
    def show_count(cls):
          # yeh print karega total objects ka count
        print("Total Object Create :",cls.count)

# Example usage:
# Jab bhi naya object banta hai, count automatically barh jata hai
c1 = Counter()  # Pehla object banaya, count 1 ho gaya
c2 = Counter()  # Dusra object banaya, count 2 ho gaya
c3 = Counter()  # Teesra object banaya, count 3 ho gaya

# Ab class method ko call kar ke total count dekhte hain
Counter.show_count()  # Output: Total objects created: 3

    