# Dunder functions in Python

#common dunder functions in pyhton are:
# __init__  -> Constructor (runs when object is created)
# __str__   -> String representation
# __len__   -> Length of object
# __add__   -> Addition
# __eq__    -> Equality check
# __doc__   -> Documentation of the function
# __name__  -> Name of the function

def chai_flavor(flavor = "masala"):
    """Return the flavor of chai.""" # Documentation of the function written in """ 
    # It should be written in the very first line of the function otherwise it doesnt works.
    return flavor

print(chai_flavor.__doc__) # Return the flavor of chai. (returns the document of the function)

print(chai_flavor.__name__) # Return the flavor of chai. ( returns the name of the functions)


# Some other built-in functions in Python


# 1. INPUT & OUTPUT FUNCTIONS


# print() -> Displays output on the screen
print("Hello, Python!")

# input() -> Takes input from the user (always returns string)
name = input("Enter your name: ")
print("Your name is:", name)


# 2. TYPE CONVERSION FUNCTIONS


# int() -> Converts value to integer
num_int = int("10")
print(num_int)

# float() -> Converts value to decimal
num_float = float("5.5")
print(num_float)

# str() -> Converts value to string
num_str = str(100)
print(num_str)


# 3. MATHEMATICAL BUILT-IN FUNCTIONS


# abs() -> Returns absolute value
print(abs(-25))

# pow() -> Raises number to power
print(pow(2, 3))

# round() -> Rounds the number
print(round(4.6))


# 4. SEQUENCE & COLLECTION FUNCTIONS


# len() -> Returns length of sequence
print(len("Python"))
print(len([1, 2, 3, 4]))

# sum() -> Returns sum of elements
print(sum([1, 2, 3]))

# max() -> Returns maximum value
print(max(3, 7, 1))

# min() -> Returns minimum value
print(min(3, 7, 1))


# 5. TYPE CHECKING FUNCTIONS


# type() -> Returns data type
print(type(10))
print(type("Hello"))

# isinstance() -> Checks type of variable
print(isinstance(10, int))
print(isinstance(10, str))


# 6. ITERATION RELATED FUNCTIONS


# range() -> Generates sequence of numbers
for i in range(1, 6):
    print(i)

# enumerate() -> Gives index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


# 7. FUNCTIONAL PROGRAMMING FUNCTIONS


# map() -> Applies function to all elements
numbers = [1, 2, 3, 4]
double_numbers = list(map(lambda x: x * 2, numbers))
print(double_numbers)

# filter() -> Filters elements based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


# 8. ZIP FUNCTION


# zip() -> Combines multiple iterables
names = ["Amit", "Neha", "Raj"]
marks = [85, 90, 88]

combined = list(zip(names, marks))
print(combined)


# 9. BOOLEAN BUILT-IN FUNCTIONS


# all() -> Returns True if all values are True
print(all([True, True, False]))

# any() -> Returns True if at least one value is True
print(any([False, True, False]))


# 10. HELP FUNCTION


# help() -> Shows documentation of a built-in function
help(len) 





