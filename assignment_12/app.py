# Static Methods
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
# that returns the Fahrenheit value.

# TemperatureConverter class define kiya
class TemperatureConverter():

    @staticmethod
    def celsius_to_fehreheit(c):

        # Ye static method Celsius ko Fahrenheit mein convert karta hai
        # Formula: (Celsius × 9/5) + 32
        return (c * 9/5) + 32
    

temp_c = 25     # Celsius temperature set kiya

# Static method ko call karke Fahrenheit value li
temp_f = TemperatureConverter.celsius_to_fehreheit(temp_c)

# Result print kiya
print(f"{temp_c}°C Is Equal to {temp_f}°C")
     