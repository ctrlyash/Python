import recipes.flavors
print(recipes.flavors.ginger_chai()) # Accessing function via module name


from recipes.flavors import elaichi_chai, ginger_chai # imports specific functions from flavors.py

print(elaichi_chai()) # Directly using the imported function


from .recipes.flavors import * # imports all functions from flavors.py (not recommended for large modules)

from recipes.flavors import ginger_chai as strong_tea # aliasing the imported function (aliasing means giving a different name to the imported function)

print(strong_tea()) # Using the aliased function


from datetime import datetime # importing from standard library