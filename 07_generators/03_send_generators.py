# Normally, yield gives output from a generator.
# But with .send(), we can also send input into a generator.


def chai_customer():
    print("Welcome ! What chai would you like to have ?")
    order = yield
    while True: # infinite loop
        print(f"Preparing: {order}")
        order = yield


stall = chai_customer()
next(stall)  # start the generator  
# Welcome ! What chai would you like to have ?


stall.send("Masala Chai")
# Preparing: Masala Chai


stall.send("Lemon Chai") 
# Preparing: Lemon Chai



# working: (comment it before running)

def chai_customer():
    # This line runs ONLY ONCE when the generator is started
    # It welcomes the customer before taking any order
    print("Welcome ! What chai would you like to have ?")

    # The generator pauses here and waits for input
    # Whatever value is sent using .send(value)
    # will be assigned to the variable 'order'
    order = yield

    # Infinite loop to keep taking orders
    while True:
        # Prints the current order received from send()
        print(f"Preparing: {order}")

        # Generator pauses again and waits for the NEXT order
        # The new value sent using .send(value)
        # replaces the old value in 'order'
        order = yield