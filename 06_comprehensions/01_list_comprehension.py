# List comprehension: List comprehension is a short and clean way to create lists in Python using a single line of code instead of a loop.

# syntax: new_list = [expression for item in iterable if condition]

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea] # name of the expression and item should be same as expression is derived from the item.

print(iced_tea) # ['Iced Lemon Tea', 'Iced Peach Tea']


new_tea = [my_tea for my_tea in menu if len(my_tea) < 12]

print(new_tea) # ['Masala Chai', 'Green Tea', 'Ginger Chai']
