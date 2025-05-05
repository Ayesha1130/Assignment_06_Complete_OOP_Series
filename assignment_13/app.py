#  Composition
# Create a class Engine and a class Car. Use composition by passing an Engine object to 
# the Car class during initialization. Access a method of the Engine class via the Car
#  class.

# Engine class define ki
class Engine():
    def start(self):

          # Jab engine start hoga to ye message print hoga
        print("Engine Started")


# Car class define kar rahe hain jo Engine object ko use karegi
class Car():
    def __init__(self,engine):

        # Car ke paas ek engine hoga (ye composition hai)
        self.engine = engine


    def start_car(self):
        # Car ko start karne par pehle ye message print hoga
        print("Starting the Car")

       # Phir engine ka start method call kiya jayega
        self.engine.start()

# Engine ka object 
my_engine = Engine()

# Car ka object bana rahe hain aur usme engine pass kar rahe hain
my_car = Car(my_engine)

# Car start kar rahe hain (jo indirectly engine start karegi)
my_car.start_car()