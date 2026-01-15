def serve_chai():
    chai_type = "Masala" # Local Scope (within the function only)
    print(f"Inside function {chai_type}") # Inside function Masala

chai_type = "Lemon"
serve_chai()
print(f"Outside function {chai_type}") # Outside function Lemon


def chai_counter():
    chai_order = "lemon" # Enclosing scope 

    def print_order():
        chai_order = "Ginger"
        print("Inner: ", chai_order) # Inner:  Ginger
    print_order()
    print("Outer: ", chai_order) # Outer:  lemon    


chai_order = "Tulsi" 
chai_counter() # Global Scope
print("Global: ", chai_order) # Global:  Tulsi  