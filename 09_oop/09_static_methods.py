 # @staticmethod is used for methods that do not depend on object or class state

# It behaves like a normal function but is grouped inside a class

class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        # text.split(",") splits the string into a list using comma as separator
        # item.strip() removes leading and trailing spaces from each item
        # list comprehension creates and returns a cleaned list
        return [item.strip() for item in text.split(",")]
    

# Raw string containing ingredients with extra spaces
raw = " water , milk , ginger , honey "

# Calling the static method directly using the class name
# No object creation is required
cleaned = ChaiUtils.clean_ingredients(raw)

# Printing the cleaned list of ingredients
print(cleaned)  # ['water', 'milk', 'ginger', 'honey']
