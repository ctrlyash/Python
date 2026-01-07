# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}") # Total grams of base tea is 17  

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaining_tea}") # Total grams of remaining tea is 11

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}") # Milk per serving is 1.75

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Whole tea bags per pot: {bags_per_pot}") #Whole tea bags per pot: 1 (Using // for division gives whole number and ignores numbers after decimal point)

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}") # Leftover C pods 1 (modulus operator in python gives the remainder of the devision.)

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor # exponential symbol (raises to power)
print(f"Scaled flavour strength {powerful_flavour}") # Scaled flavour strength 8 (2*2*2)

total_tea_leaves_harvested = 1_000_000_000 # These underscores can be used like this to write large numbers.
print(f"Tea leaves: {total_tea_leaves_harvested}") # Tea leaves: 1000000000 (It only improves the readability and does not bother python.)