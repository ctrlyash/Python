# Tuples: ()

masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}") # Main masala spices: cardamom, cloves, cinnamon (values of masala_spices tuple are assigned to new tuple.)


ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cardamom_ratio}") # Ratio is G: 2 and C: 1


ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio 
print(f"Ratio is G: {ginger_ratio} and C: {cardamom_ratio}") # Ratio is G: 1 and C: 2
# we can swap variables in Python like this.



# Membership: used to test if a particular string is a member of any tuple using 'in' keyword

print(f"Is ginger in masala spices? {'ginger' in {masala_spices}}") # Is ginger in masala spices? False

print(f"Is Cardamom in masala spices? {'Cardamom' in {masala_spices}}") # Is Cardamom in masala spices? False (Membership is case sensetive.)
