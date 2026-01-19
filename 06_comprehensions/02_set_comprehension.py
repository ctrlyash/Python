# Set comprehension: It is a short and clean way to create a set using one line of code, similar to list comprehension, but it stores only unique values.
# syntax: new_set = {expression for item in iterable if condition}

favourite_chai = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chai}
print(unique_chai) # {'Elaichi Chai', 'Green Tea', 'Masala Chai', 'Lemon Tea'} (collection of ordered unique items)

unique_chai = {chai for chai in favourite_chai if len(chai) < 8}
print(unique_chai) # set() (empty set as all are greater than 8)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"] 
} # a dictionary

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients} # in this type of cases whatever the final item we are giving is derived as expression for eg. spice

print(unique_spices) # {'black pepper', 'ginger', 'clove', 'milk', 'cardamom'}