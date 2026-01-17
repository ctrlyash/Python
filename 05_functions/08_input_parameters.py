chai = "Ginger chai"

def prepare_chai(order):
    print("Perparing ", order)

prepare_chai(chai) # Perparing  Ginger chai
print(chai) # Ginger chai (value of variable remains unchanged as string is immutable)



chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai) # [1, 42, 3]
print (chai) # [1, 42, 3] (value of variable changes as list is mutable)



def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # positional arguments (passed in the order of parameters)
# Darjeeling Yes Low

make_chai(tea="Green", sugar="Medium", milk="Yes") # keyword arguments (no need to pass in the order of parameters)
# Green Yes Medium



def special_chai(*ingredients, **extras): # *args and **kwargs (* for arguments and ** for keyword arguments)
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("ginger", "cardamom", "black tea", size="Large", sugar=2)
# Ingredients ('ginger', 'cardamom', 'black tea')
# Extras {'size': 'Large', 'sugar': 2}    



def chai_orders(order=[]):
    order.append("Masala chai")
    print(order)

chai_orders() # ['Masala chai']
chai_orders() # ['Masala chai', 'Masala chai']



def chai_orders(order=None):
    if order is None:
        order = []
        print(order)

chai_orders() # []
chai_orders() # [] (both times empty list is printed as order is None)

 