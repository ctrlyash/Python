# A tea stall offers different prices for different cup sizes. Write a program that calculates the price based on size.
# Task:
# Input: "small", "medium", "large"
# Small → 10, Medium ₹15, Large →₹20
# If invalid: show "Unknown cup size"

cup = input("Choose your cup size(small, medium, large): ").lower()

if cup == "small":
    print("Price: 10")
elif cup == "medium":
    print("Price: 15")
elif cup == "large":
    print("Price: 20")
else:
    print("Unknown cup size")

# Choose your cup size(small, medium, large): Large  
# Price: 20

