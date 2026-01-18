# Pure and Impure functions

def pure_chai(cups): # pure function as it does not modify any external variable
    return cups * 10

total_chai = 0 

# not recommended
def impure_chai(cups): # impure function as it modifies the global variable
    global total_chai 
    total_chai += cups  
    return total_chai


# Recursive function

def pour_chai(n):
    print("Pouring cup ", n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(5)) 
# Pouring cup  5
# Pouring cup  4 
# Pouring cup  3
# Pouring cup  2
# Pouring cup  1
# Pouring cup  0
# All cups poured 


# Lambda function: A lambda function in Python is a small anonymous (nameless) function written in one line, used for short and simple operations.
# No return keyword (it returns automatically)
# syntax --> lambda arguments : expression


chai_types = ["Light", "Kadak", "Ginger", "Kadak"]

strong_chai = list(filter(lambda chai: chai == "Kadak", chai_types))

print(strong_chai) # ['Kadak', 'Kadak']


non_strong_chai = list(filter(lambda chai: chai != "Kadak", chai_types))

print(non_strong_chai) # ['Light', 'Ginger']