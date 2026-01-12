# You're preparing an order summary with customer names and their total bill.
# Task:
# Use two lists: one for names and one for bills.
# • Print: "[Name] paid [amount]"

names = ["Rahul", "Yash", "Siddharth", "Virat", "Rohit"]
bills = [100, 200, 300, 400, 500]

for name, amount in zip(names, bills): # zip combines multiple iterables (like lists, tuples, sets, etc.) element by element and returns an iterator of tuples.
    print(f"{name} paid {amount}")

# Rahul paid 100
# Yash paid 200
# Siddharth paid 300
# Virat paid 400
# Rohit paid 500    