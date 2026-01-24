# Ways to access the base class constructor in Python

class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# code repetition in subclass
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level = spice_level

# Instead of redefining the attributes in the subclass, we can explicitly call the parent class's constructor.

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        self.spice_level = spice_level 



# Instead of redefining the attributes in the subclass, we can use super() to call the parent class's constructor.

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level

# this one is similar to the previous one but it is more maintainable and cleaner.  
