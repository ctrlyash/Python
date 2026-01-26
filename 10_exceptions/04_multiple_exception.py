def process_order(item, quantity):
    try:
        price = {"masala": 20}[item] # whatever key is asked for goes in the square brackets and returns the value

        if not isinstance(quantity, int):
                raise TypeError("Quantity must be a number.") # we need to write this if code to prevent operator overloading otherwise the given string will be concatenated and 20*'two' will be printed.
        
        # Just like this we can also raise our custom erroes usinf raise keyword.
        
    except KeyError:
        print("Sorry, we do not have that item.")    
    except TypeError as te:
        print(te)  # executes if TypeError occurs
    else:    
            cost = price * quantity  
            print(f"Total cost is {cost}")
     
    

    
process_order("masala", 2)  # total cost is 40      
process_order("green", 2)  # Sorry, we do not have that item.    
process_order("masala", "two")  # Quantity must be a number.            