# Mutable and Immutable objects 

# Immutable: An immutable object is an object whose value cannot be changed after creation.
# If you try to change it → Python creates a new object instead.
# Common immutable types-
# int
# float
# bool
# str
# tuple
 #frozenset

# for eg-

sugar_amount = 2
print(f"Initial sugar: {sugar_amount}") # Initial sugar: 2
print(f"ID of 2: {id(2)}") # ID of 2: 140714275337368

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}") # Second Initial sugar: 12 

print(f"ID of 2: {id(2)}") # ID of 2: 140714275337368 (2 remains the same)
print(f"ID of 12: {id(12)}") # ID of 12: 140714275337688 


# Mutable: A mutable object is an object whose value can be changed after creation, without creating a new object.
# Common mutable types
# list
# dict
# set
# bytearray

# for eg-

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}") # Initial spice mix id: 1441057376512
print(f"Initial spice mix id: {spice_mix}") # Initial spice mix id: set()

spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")
print(f"Initial spice mix id: {spice_mix}") # Initial spice mix id: {'Ginger', 'lemon', 'cardamom'}
print(f"After spice mix id: {id(spice_mix)}") # After spice mix id: 1441057376512 (inital id remains same even after changing the set values.)