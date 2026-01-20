# using yield for taking values from different functions using fraom keyword.

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"


def full_menu():
    yield from local_chai()   
    yield from imported_chai()   

for chai in full_menu():
    print(chai)

# Masala Chai
# Ginger Chai
# Matcha
# Oolong


# .close (stops the generator)
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")


stall = chai_stall()
print(next(stall))
# Waiting for chai order
# Stall closed, No more chai

stall.close() 
#  good practice memory cleanup
# it is a generator exit
