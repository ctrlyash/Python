# Some common errors in Python

# IndexError example
orders = ["masala", "ginger"]
print(orders[2])  
# IndexError: list index out of range


# ZeroDivisionError example
price = 100
print(price / 0)  
# ZeroDivisionError: division by zero


# ValueError example
quantity = int("chai")
print(quantity)  
# ValueError: invalid literal for int() with base 10


# TypeError example
total = "10" + 5
print(total)  
# TypeError: can only concatenate str (not "int") to str


# KeyError example
menu = {"tea": 10, "coffee": 20}
print(menu["chai"])  
# KeyError: 'chai'


# NameError example
print(order_type)  
# NameError: name 'order_type' is not defined


# AttributeError example
drink = "chai"
drink.push("hot")  
# AttributeError: 'str' object has no attribute 'push'


# FileNotFoundError example
file = open("bill.txt")  
# FileNotFoundError: [Errno 2] No such file or directory: 'bill.txt'


# These errors can be handled using try-except blocks to prevent program crashes.