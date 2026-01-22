class Chai:
    origin = "India" # whenever a variable is defined inside a class but outside any method, it is called a class variable or property.

print(Chai.origin)  # India (Accessing class variable directly from the class)

Chai.is_hot = True  # Dynamically adding a new class variable
print(Chai.is_hot)  # True

# creating objects from class Chai

masala = Chai()
print(f"Masala{masala.origin}") # Masala India (Accessing class variable from an instance)
print(f"Masala{masala.is_hot}") # Masala True 

masala.is_hot = False



print(f"Masala{masala.is_hot}") # Masala False (Instance variable overrides class variable for this instance)

print("Class: ", Chai.is_hot) # Class:  True (Class variable remains unchanged)


masala.flavor = "spicy"
print(masala.flavor) # spicy (Instance variable specific to masala instance)
 