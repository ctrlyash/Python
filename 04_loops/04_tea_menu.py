# You're creating a tea menu board. Each item must be numbered.
# Task:
# • Use enumerate() to print menu items with numbers

menu = ["Black", "Green", "Milk", "Masala"]

for idx, item in enumerate(menu, start= 1): # In python indexing always start from zero, so we define the start value.
    print(f"{idx}: {item} Tea") 

# 1: Black Tea
# 2: Green Tea
# 3: Milk Tea
# 4: Masala Tea    