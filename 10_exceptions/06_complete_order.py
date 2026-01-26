# Proper example of handling multiple exceptions and using finally block.

class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {
        'masala': 50,
        'ginger': 60
    }
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai flavor is not available.")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer.")


        total = menu[flavor] * cups
        print(f"Total bill for {cups} cups of {flavor} is {total}")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Thank you for visiting our chai shop!")

bill("mint",3)
bill("ginger","two")
bill("masala",2)            

# Error: That chai flavor is not available.
# Thank you for visiting our chai shop!
# Error: Number of cups must be an integer.
# Thank you for visiting our chai shop!
# Total bill for 2 cups of masala is 100
# Thank you for visiting our chai shop! 