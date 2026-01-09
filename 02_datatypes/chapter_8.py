essential_spices = {"cardamom", "ginger", "cinnamom"}
optional_spices = {"cloves", "ginger", "black pepper"}

# union
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}") # All spices: {'cloves', 'cinnamom', 'ginger', 'black pepper', 'cardamom'}

# intersection
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}") # common spices: {'ginger'}

# difference
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices {only_in_essential} ") # Only in essential spices {'cinnamom', 'cardamom'} 

# membership testing
print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}") # Is 'cloves' in essential spices? False

# symmetric difference
unique_spices = essential_spices ^ optional_spices
print(f"Unique spices (not common): {unique_spices}")


