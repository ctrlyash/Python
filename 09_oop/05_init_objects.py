# A constructor in Python is a special method that is automatically called when an object is created from a class.
# It is mainly used to initialize (set up) object data.

class ChaiOrder():
    def __init__(self, type_, size): # __init__() is used to initialize the constructor 
    # first parameter is always self    
        self.type = type_ # we used type_ beacuse type is a reserved function in python.
        self.size = size
        # we should keep the names same for clarity and convention (not compulsary)
        

    def summary(self):
        return f"{self.size}ml of {self.type} chai"    



order = ChaiOrder("Masala", 200)
print(order.summary()) # 200ml of Masala chai


order_two = ChaiOrder("Ginger", 250)
print(order_two.summary()) # 250ml of Ginger chai

