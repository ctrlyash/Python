# Custom Exception
class OutOfIngredientsError(Exception): # inheriting from built-in Exception class
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Cannot make chai, ingredients are out!")
    print("Chai is ready!")

make_chai(0, 1)  # Raises OutOfIngredientsError: Cannot make chai, ingredients are out!