# Inheritance: it is a mechanism where a new class inherits properties and behavior (methods) from an existing class.

# Composition: it is a design principle where a class is composed of one or more objects from other classes, allowing for more flexible code reuse.

class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")  

class MasalaChai(BaseChai): # Inheriting from BaseChai
    def add_spices(self):
        print("Adding cardmom, ginger, cloves.")


class ChaiShop:
    chai_class = BaseChai  # Default chai class (we can access whole class using class variable)
    def __init__(self):
        self.chai = self.chai_class("Regular")  # Creating an instance of the chai class

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")  # Serving Regular chai in the shop
        self.chai.prepare()  # Preparing Regular chai...


class FancyChaiShop(ChaiShop):
    chai_class = MasalaChai  # Overriding the chai class to MasalaChai
              


shop = ChaiShop() 

fancy = FancyChaiShop()

shop.serve() # Serving Regular chai in the shop

fancy.serve() # Preparing Regular chai...

# Now, let's use the add_spices method from MasalaChai

fancy.chai_class.add_spices() # TypeError: chai_class.add_spices() missing 1 required positional argument: 'self'

# this error occurs because we have stored chai_class in 'chai' variable not in object variable.

fancy.chai.add_spices()  # Adding cardmom, ginger, cloves.       