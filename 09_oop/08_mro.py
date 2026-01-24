# Method Resolution Order (MRO) in Python

class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(B, C):
    pass

cup = D()
print(cup.label) # B: Masala blend

# whichever class comes first in the inheritance list that class's attribute is given preference.

cup = D(C, B)
print(cup.label) # C: Herbal blend


print(D.__mro__)
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>] # Method Resolution Order 

# (not generally used directly but useful for understanding the order of attribute/method lookup in multiple inheritance scenarios)