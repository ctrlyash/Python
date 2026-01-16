# Nonlocal: Normally, if you change a variable inside a function, Python treats it as local.
# But sometimes you want to modify a variable from the outer (enclosing) function — that’s when nonlocal is used.


def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type # access chai_type from just outside the inner function.
        chai_type = "Kesar"
    #kitchen()  
    print("After kitchen update", chai_type) 
update_order()     

# After kitchen update Kesar



# Global: global is a keyword in Python used inside a function to tell Python that a variable belongs to the global (outside) scope, not the local function.

name_cricketer = "Virat Kohli"

def local_fun():

    def player_name():
        global name_cricketer # helps accessing name_cricketer from outside the outer function.
        name_cricketer = "Rohit Sharma"
    player_name()
    print(name_cricketer)

local_fun()

# Rohit Sharma