class Chai: # Creating a class
    pass

class ChaiTime:
    pass


print(type(Chai)) # <class 'type'>  # The 'type' is the metaclass for all classes in Python

ginger_tea = Chai()  # Creating an instance of the Chai class

print(type(ginger_tea))  # <class '__main__.Chai'>  # The instance is of type Chai

print(type(ginger_tea) is Chai) #  True

print(type(ginger_tea) is ChaiTime) # False