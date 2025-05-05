#  Make a Custom Class Iterable
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() 
# to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        # Starting point set kar rahe hain
        self.start = start
        self.current = start  # initial current value set kar rahe hain

    def __iter__(self):
        # Ye method iterable banata hai
        return self

    def __next__(self):
        # Har next iteration pe current value ko return karenge
        if self.current > 0:
            self.current -= 1  # Countdown karte hain
            return self.current + 1  # value return karte hain
        else:
            # Jab countdown 0 par pohanch jaye, to StopIteration raise karenge
            raise StopIteration

# Object bana rahe hain Countdown class ka, start value 5 se
countdown = Countdown(5)

# For loop mein iterate karenge
for num in countdown:
    print(num)
