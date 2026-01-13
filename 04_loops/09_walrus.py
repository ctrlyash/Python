# Walrus operator(:=) : The walrus operator (:=) in Python is used to assign a value to a variable and use it in the same expression.

# Normal if condition example
value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible, remainder is {remainder}")
# Not divisible, remainder is 3


# Using walrus operator
value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")
# Not divisible, remainder is 3


# Another walrus example
available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your tea cup size: ").lower()) in available_sizes:
    print(f"Your cup size is {requested_size}")
else:
    print(f"Size is unavailable - {requested_size}")    

# Enter your tea cup size: tester
# Size is unavailable - tester



flavours = ["masala", "ginger", "lemon","mint"]

print(f"Available flavours: {flavours}")

while (flavour := input("Choose your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} is not available")

print(f"You choose {flavour} chai")

# Choose your flavour: Cardamom
# Sorry, Cardamom is not available
# Choose your flavour: masala
# You choose masala chai