# Dictionaries {key: value}: dictionary in python is a collection of key-value pairs.

# this is how we define a dictionary
chai_order = dict(type="Masala  Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}") # Chai order: {'type': 'Masala  Chai', 'size': 'Large', 'sugar': 2}

# another way to define a dictionary
chai_recipe = {} 
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# Accessing elements in a dictionary
print(f"Recipe base: {chai_recipe['base']}") # Recipe base: black tea
print(f"Recipe: {chai_recipe}") # Recipe: {'base': 'black tea', 'liquid': 'milk'}

# deleting elements
del chai_recipe['liquid']
print(f"Recipe: {chai_recipe}") # Recipe: {'base': 'black tea'}

# Membership testing (in)
print(f"Is sugar in the order? {'sugar' in chai_order}") # Is sugar in the order? True


# Dictionary methods

chai_order = {"type": "Ginger Chai", "size": "Medium", "suagr": 1, "price": 10}

# keys(): Returns a list of all the keys in the dictionary
print(f"Order details (keys): {chai_order.keys()}") # Order details (keys): dict_keys(['type', 'size', 'suagr', 'price'])

# values(): Returns a list of all the values in the dictionary
print(f"Order details (values): {chai_order.values()}") # Order details (values): dict_values(['Ginger Chai', 'Medium', 1, 10])

# items(): Returns a list of all the (key, value) tuples in the dictionary
print(f"Order details (items): {chai_order.items()}") # Order details (items): dict_items([('type', 'Ginger Chai'), ('size', 'Medium'), ('suagr', 1), ('price', 10)])

# pop(): Removes the specified key from the dictionary and returns the value
pop_item = chai_order.pop("suagr")
print(f"Removed item: {pop_item}") # Removed item: 1

# popitem(): Removes the last item from the dictionary and returns it
last_item = chai_order.popitem()
print(f"Removed Last item: {last_item}") # Removed Last item: ('price', 10)

# update(): Updates the dictionary with the key-value pairs from another dictionary
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated recipe: {chai_recipe}") # Updated recipe: {'base': 'black tea', 'liquid': 'milk', 'cardamom': 'crushed', 'ginger': 'sliced'}

# size(): Returns the number of items in the dictionary
chai_size = chai_order["size"]
print(f"Chai size: {chai_size}") # Chai size: Medium

# get(): Returns the value of the specified key if it exists, otherwise returns the default value
customer_note = chai_order.get("note", "No note provided")
print(f"Customer note: {customer_note}") # Customer note: No note provided

customer_note = chai_order.get("size", "No note provided")
print(f"Customer note: {customer_note}") # Customer note: Medium


# copy(): Creates a shallow copy of the dictionary
copy_order = chai_order.copy()
print(f"Copy order: {copy_order}") #Copy order: {'type': 'Ginger Chai', 'size': 'Medium'}

# setdefault(): Returns the value of the specified key if it exists, otherwise returns the default value
chai_order.setdefault("price", 10)
print(f"Chai order: {chai_order}") # Chai order: {'type': 'Ginger Chai', 'size': 'Medium', 'price': 10}

# clear(): Removes all items from the dictionary
chai_order.clear()
print(f"Chai order: {chai_order}") # Chai order: {}

# fromkeys(): Creates a new dictionary with the specified keys and assigns same values to all keys
keys = ["qty_masalaTea", "qty_blackTea", "qty_greenTea"]
new_dict = dict.fromkeys(keys, 1)
print(f"New dictionary: {new_dict}") # New dictionary: {'qty_masalaTea': 1, 'qty_blackTea': 1, 'qty_greenTea': 1}