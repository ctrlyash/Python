# @classmethod : A class method is a method that works with the class itself using cls instead of an instance using self.

# acts as an alaternative constructor when ypu want to call constructor again and again.


# @classmethod
# - Uses 'cls' as first argument
# - Works with class variables
# - Used for class-level behavior

# @staticmethod
# - Uses no 'self' or 'cls'
# - Independent of class and object data
# - Used for utility/helper functions


class ChaiOrder:
    def __init__(self, tea_type, sweetness, size): # regular constructor
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data['tea_type'],
            order_data['sweetness'], 
            order_data['size']
        )    
    
    @classmethod # creating alternative constructor
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size.lower() in ['small', 'medium', 'large']
    
print(ChaiUtils.is_valid_size('Medium'))  # True  (calling static method without creating object for utility function like validation)
    

order1 = ChaiOrder.from_dict({
    'tea_type': 'Masala',
    'sweetness': 'medium',
    'size': 'large'    
}) # creating object using class method as alternative constructor  

order2 = ChaiOrder.from_string("Ginger-low-small")

order3 = ChaiOrder("Large", 'Low', 'Large')

print(order1.__dict__) # {'tea_type': 'Masala', 'sweetness': 'medium', 'size': 'large'} 

print(order2.__dict__) # {'tea_type': 'Ginger', 'sweetness': 'low', 'size': 'small'} (we can get ouput of any type in form of dictionary using dunder __dict__)

print(order3.__dict__) # {'tea_type': 'Large', 'sweetness': 'Low', 'size': 'Large'}

# @classmethod is used for methods that operate on the class itself rather than on instances