# Boolean: In Python, a boolean is a data type that represents one of two values: True or False.

is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling
print(f"Total actions: {total_actions}") # Total actions: 6
# Here we see that is_boiling data type is chnaged to integer which means True is chnaged to 1.
# This is known as Upcasting

milk_present = 0
print(f"Is there milk? {bool(milk_present)}") # False

# some values alwways return false in pyhton.
# False
# None
# 0
# 0.0
# 0j
# ""          # empty string
# []          # empty list
# ()          # empty tuple
# {}          # empty dict
# set()       # empty set

# Rest all values return True for eg: " " gives True


# and => AND is a logical operator that returns true only when all given conditions are true; otherwise it returns false.
# for eg:

water_hot = True
tea_added = False
can_serve = water_hot and tea_added
print(f"Can serve tea? {can_serve}") # Can serve tea? False

water_hot = True
tea_added = True
can_serve = water_hot and tea_added
print(f"Can serve tea? {can_serve}") # Can serve tea? True

# or: A logical operator that returns true if at least one condition is true.
# for eg:

milk_available = False
coffee_powder = True

can_make_coffee = milk_available or coffee_powder
print(f"Can make coffee? {can_make_coffee}")  # Can make coffee? True

# not: A logical operator that reverses the boolean value of a condition (true becomes false, false becomes true).
# for eg

door_locked = False

can_enter = not door_locked
print(f"Can enter room? {can_enter}")  # Can enter room? True

