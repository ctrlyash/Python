# You want to skip those and stop entirely if someone requests a restricted flavor.
# Task:
# • Skip if flavor is "Out of Stock"
# • Break if flavor is "Discontinued"

flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]


for flavour in flavours:
    if flavour == "Out of Stock":
        continue # (skips out of stock)
    if flavour == "Discontinued":
        print(f"{flavour} item found") # (including this print statement in if prints ginger and lemon)
        break # (breaks the loop)
    print(f"{flavour} item found")

print(f"Out side of loop")

# Ginger item found
# Lemon item found
# Discontinued item found
# Out side of loop