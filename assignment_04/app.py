# Class Variables and Class Methods
# Create a class Bank with a class variable bank_name. Add a class method 
# change_bank_name(cls, name) that allows changing the bank name. Show that 
# it affects all instances.

class Bank():
       # Class variable (sab objects ke liye common hota hai)
    bank_name = "UBL"

    # Class method jo bank ka naam change karega
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name # class variable ko update kar rahe hain

# 2 objects create karte hain
account1 = Bank()
account2 = Bank()

# Dono objects ka bank name print kiya
print("Before Change")
print(" Bank Account 1 :" ,account1.bank_name)
print(" Bank Account 2 :", account2.bank_name)

# Ab class method use karke bank ka naam change kiya
Bank.change_bank_name("National Bank of Pakistan")

# Dubara dono objects ka bank name check kiye
print("\nAfter Change")
print(" Bank Account 1 :" ,account1.bank_name)
print(" Bank Account 2 :", account2.bank_name)


