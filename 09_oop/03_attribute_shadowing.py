# Attribute: variable inside an object is known as attribute

# Attribute shadowing: Attribute shadowing is the process in which a subclass attribute hides an attribute of the same name in its parent class.

class Chai:
    temperature = "Hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temperature) # Hot

cutting.temperature = "Mild"
# A new instance attribute temperature is created
# This shadows the class attribute
# Now Python uses the object’s version, not the class’s
# This is attribute shadowing

print("After changing ",cutting.temperature) # After changing Mild

print("Direct look into the class ",Chai.temperature) # Direct look into the class Hot


del cutting.temperature
print(cutting.temperature) # Hot (if the object is deleted or not available the attribute falls back to class and gives the defualt result as it was just shadowing the class property. )



cutting.cup = "Small"

print("Cup size is  ",cutting.cup) # Cup size is Small

del cutting.cup
print(cutting.cup) # AttributeError: 'Chai' object has no attribute 'cup'

# cup exists only in the object
# The class has no cup attribute
# Therefore this is not shadowing.



