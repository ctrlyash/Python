chai_menu = {
    'Masala': 50,
    'Green': 40,
}
chai_menu["elaichi"] # KeyError: 'elaichi' (this key does not exist in dictionary)
# (comment out above line to run the rest of the code)

print("Hello python...") # This line will not be executed due to the unhandled exception above

try:
    chai_menu = {"elaichi"}
except KeyError:
    print("The key which you are trying to access does not exists.")   

print("Hello python...") # This line will be executed as the exception is handled