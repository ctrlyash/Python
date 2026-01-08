# List: []

ingredients = ["water", "milk", "black tea"]
print(f"Ingredients are: {ingredients}") # Ingredients are: ['water', 'milk', 'black tea']


ingredients.append("sugar")
print(f"Ingredients are: {ingredients}") # Ingredients are: ['water', 'milk', 'black tea', 'sugar']
# Append always adds the value to the very end of the list


ingredients.remove("water")
print(f"Ingredients are: {ingredients}") # Ingredients are: ['milk', 'black tea', 'sugar']
# Remove allows us to remove the desired item from list by passing VALUE not index.


spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", 'milk']
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}") # chai: ['water', 'milk', 'ginger', 'cardamom']
# We can add different lists using extend method.


chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}") # chai: ['water', 'milk', 'black tea', 'ginger', 'cardamom'] (new wvalue was inserted at 2 index and the elements shifted to right)
# Insert allows you to insert the value at the desired position.


last_added = chai_ingredients.pop()
print(f"{last_added}") # cardamom (last item poped and returned)
print(f"{chai_ingredients}") # ['water', 'milk', 'black tea', 'ginger'] (last item is removed from thr array after pop)
# pop() in deafult removes the last item from the list and gives it as output when printed.


# Similarly, pop can be given index as attribute to remove the specific item at any particular index.

second_added = chai_ingredients.pop(1)
print(f"{second_added}") # milk (item at first index removed and returned)
print(f"{chai_ingredients}") # ['water', 'black tea', 'ginger']  (item at the 1st index was removed from the list after pop(1))



print(f"{chai_ingredients}") # ['water', 'black tea', 'ginger']
chai_ingredients.reverse()
print(f"{chai_ingredients}") # ['ginger', 'black tea', 'water']
# reverse() reverses the complete list.


chai_ingredients.sort()
print(f"{chai_ingredients}") # ['black tea', 'ginger', 'water']
# sort() sorts the list alphabeticaly.


sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level:{max(sugar_levels)}") # Maximum sugar level:5
# Max gives the maximum value in the list.

print(f"Minimum sugar level:{min(sugar_levels)}") # Minimum sugar level:1
# Min gives the minimum value in the list.



# Operator overloading: Operation overloading means using the same operator (+, -, *, etc.) for different purposes depending on the objects.

base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}") # Liquid mix: ['water', 'milk', 'ginger']

strong_brew = ["black tea"] * 3
print(f"Strong brew: {strong_brew}") # Strong brew: ['black tea', 'black tea', 'black tea']

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}") # Strong brew: ['black tea', 'water', 'black tea', 'water', 'black tea', 'water']


# we can use more operations using-
from operator import itemgetter # we may talk about it later.


# bytearray: A bytearray in Python is a mutable sequence of bytes—that is, an ordered collection of integers where each value is in the range 0–255, and the contents can be changed after creation.

raw_spice_data = bytearray(b"CINNAMON")
print(f"Bytes: {raw_spice_data} ") # Bytes: bytearray(b'CINNAMON') 

raw_spice_data = raw_spice_data.replace(b"CINNA", B"CARD")
print(f"Bytes: {raw_spice_data} ") # Bytes: bytearray(b'CARDMON') 



