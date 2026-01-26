def serve_chai(flavor):
    try:
        print(f"Preparing your {flavor} chai...")
        if flavor == "unknown": 
            raise ValueError("Flavor not recognized!") 
    except ValueError as ve:
        print(f"Error: {ve}") # executes if ValueError occurs

    else:
        print(f"{flavor} chai is ready to be served!") # executes if no exception occurs

    finally:
        print("Next Customer, please!")  # always executes


serve_chai("Masala")
serve_chai("unknown")     

# Preparing your Masala chai...
# Masala chai is ready to be served!
# Next Customer, please!
# Preparing your unknown chai...
# Error: Flavor not recognized!
# Next Customer, please!