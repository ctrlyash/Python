# @property is used to define methods that can be accessed like attributes while providing controlled access to object data. (Access control)

class TeaLeaf:
    def __init__(self, age):
        self. _age = age # private attribute (conventionally anything with _ is considered private and has to be accessed via getter and setter methods)


    @property
    def age(self):
        return self._age + 2 # adding 2 years of aging process
    
    @age.setter
    def age(self, new_age):
        if 1 <= new_age <= 5:
            self._age = new_age
        else:
            raise ValueError("Age must be between 1 and 5 years.")

leaf = TeaLeaf(3)
print(leaf.age)  # Output: 5 
 
leaf.age = 6
print(leaf.age) # ValueError: Age must be between 1 and 5 years.         