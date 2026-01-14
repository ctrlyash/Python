# Reducing Code Duplication

# You're managing a busy tea stall.
# You recieve many orders and want to print each customer's name along with the type of chai they ordered.
# Task:
# Use a function print_order(name, chai_type)
# Call it multiple times for customers.

def print_order(name, chai_type): # here name and chai_type are parameters
    print(f"{name} ordered {chai_type} chai!")

print_order("Rahul", "Black") # here Rahul and Black are arguments
print_order("Yash", "Green")
print_order("Rishabh", "Milk")
print_order("Virat", "Masala")
print_order("Rohit", "Black")

# Rahul ordered Black chai!
# Yash ordered Green chai!
# Rishabh ordered Milk chai!
# Virat ordered Masala chai!
# Rohit ordered Black chai!

# Parameters are passed when defining the function
# Arguments are passed when calling the function