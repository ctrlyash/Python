def make_chai():
    return "Here is your Masala chai"

return_value = make_chai()

print(return_value) # Here is your Masala chai
def make_chai():
    print("Here is your Masala chai")

return_value = make_chai()

print(return_value) # None


# Case 1 - returning nothing
def idle_chiwala():
    pass

print(idle_chiwala()) # None (we returned nothing)


# Case 2 - retuening one value
def sold_cups():
    return 120

total = sold_cups()
print(total) # 120


# returning early from a function
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"

print (chai_status(0)) # Sorry, chai over (exits the iteration)
print (chai_status(10)) # Chai is ready


# Returning multiple values
def chai_reports():
    return 100, 20, 10 # sold, remaining

sold, remaining, not_paid = chai_reports()
print("Sold: ", sold ) # 100
print("Remaining: ", remaining) # 20
print("Not paid: ", not_paid) # 10
