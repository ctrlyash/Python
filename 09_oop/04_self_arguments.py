# self is a reference to the current object of a class.
# It allows an object to access its own variables (attributes) and methods.

class Chaicup:
    size = 150 #ml

    def describe(self): # func inside a class is known as method.
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe()) # A 150ml chai cup

print(Chaicup.describe()) # TypeError: Chaicup.describe() missing 1 required positional argument: 'self'

# to resolve this error we need to pass the object name with the method.

print(Chaicup.describe(cup)) # A 150ml chai cup

# simillarly

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two)) # A 100ml chai cup
