# set: {} A set in Python is an unordered collection of unique elements. It does not allow duplicate values.

essential_spices = {"cardamom", "ginger", "cinnamom"}
optional_spices = {"cloves", "ginger", "black pepper"}

# Set Operators

# union operator (|)
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}") # All spices: {'cloves', 'cinnamom', 'ginger', 'black pepper', 'cardamom'}

# intersection operator (&)
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}") # common spices: {'ginger'}

# difference operator (-)
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices {only_in_essential} ") # Only in essential spices {'cinnamom', 'cardamom'} 

# symmetric difference operator (^)
unique_spices = essential_spices ^ optional_spices
print(f"Unique spices (not common): {unique_spices}") # Unique spices (not common): {'black pepper', 'cardamom', 'cloves', 'cinnamom'}

# Subset operator (<=)
is_subset = essential_spices <= optional_spices
print(f"Is essential_spices a subset of optional_spices? {is_subset}") # Is essential_spices a subset of optional_spices? False

# Proper subset operator (<)
is_proper_subset = essential_spices < optional_spices
print(f"Is essential_spices a proper subset of optional_spices? {is_proper_subset}") # Is essential_spices a proper subset of optional_spices? False

# Superset operator(>=)
is_superset = essential_spices >= optional_spices
print(f"Is essential_spices a superset of optional_spices? {is_superset}") # Is essential_spices a superset of optional_spices? False

# Proper superset operator(>)
is_proper_superset = essential_spices > optional_spices
print(f"Is essential_spices a proper superset of optional_spices? {is_proper_superset}") # Is essential_spices a proper superset of optional_spices? False

# Equal operator (==)
is_equal = essential_spices == optional_spices
print(f"Are both sets equal? {is_equal}") # Are both sets equal? False

# not equal operator (!=)
is_not_equal = essential_spices != optional_spices
print(f"Are the sets different? {is_not_equal}") # Are the sets different? True

# membership testing (in)
print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}") # Is 'cloves' in essential spices? False


# Set Functions:

# add(): Adds one element to the set
s = {1, 2, 3}
s.add(4)
print(s) # {1, 2, 3, 4}

# update(): Adds multiple elements (from list, tuple, set).
s = {1, 2}
s.update([3, 4, 5])
print(s) # {1, 2, 3, 4, 5}

# remove(): Removes an element
s = {1, 2, 3}
s.remove(2) # Raises error if element not present in the set.
print(s) # {1, 3}

# discard(): Removes an element
s = {1, 2, 3}
s.discard(5) # No error if element not present in the set. set remians unchanged 
print(s) # {1, 2, 3}

# pop(): Removes random element (because set is unordered)
s = {1, 2, 3}
s.pop()
print(s) # {2, 3}

# clear(): Removes all elements
s = {1, 2, 3}
s.clear()
print(s)   # set()

# copy(): Creates a shallow copy
s1 = {1, 2}
s2 = s1.copy()
print(s2) # {1, 2}


A = {1, 2}
B = {2, 3}

# union(): Returns combined elements
print(A.union(B)) # {1, 2, 3}

# intersection(): Returns common elements
print(A.intersection(B)) # {2}

# difference(): Elements in first set only
print(A.difference(B)) # {1}

# symmetric_differnce(): Elements not common
print(A.symmetric_difference(B)) # {1, 3}

# issubset(): Checks subset
C = {1}
print(C.issubset(A)) # True

# issuperset(): Checks superset
print(A.issuperset(C)) # True

# isdisjoint(): Checks if no common elements
X = {1, 2}
Y = {3, 4}
print(X.isdisjoint(Y))  # True


# Frozen set: A frozenset is an immutable version of a set in Python.
#Once created, its elements cannot be added, removed, or changed.
# can be used as a dictionary key or inside another set

fs = frozenset([1, 2, 3])
print(fs)




