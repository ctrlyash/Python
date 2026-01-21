# Decorator: Decorators in Python are special functions that modify or extend the behavior of another function without changing its actual code.

from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper    

@my_decorator
def greet():
    print("Hello! we are learning decorators")

greet()  

# Before the function call.
# Hello! we are learning decorators
# After the function call.

print(greet.__name__) # wrapper (name of greet() changes as we've returned wrapper)


# To preserve the name we use external library functools and import wraps from it.
# We need to call it as @wraps(func) just above the func name you want to preserve.
# After this the ouput is greet.