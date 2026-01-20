# Generators are a simple and powerful tool for creating iterators.
# A generator is a function that uses the 'yield' statement to return data.
# It is a memory efficient operation i.e. you save memory by not st oring the entire list in memory.
# you don't wwant the result immedately
#lazy evaluation

# for eg:
def serve_chai():
    yield "Cup 1: Masala Chai"
    yield" Cup 2: Ginger Chai"
    yield "Cup 3: Cardamom Chai"

stall = serve_chai()

for cup in stall:
    print(cup)

# Cup 1: Masala Chai
#  Cup 2: Ginger Chai
# Cup 3: Cardamom Chai    




# normal function

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"] 


# genrator function

def get_chai_gen():
    yield "Cup1 "
    yield "Cup2 "
    yield "Cup3 "

chai = get_chai_gen()
print(chai) # <generator object get_chai_gen at 0x0000024808D85480> (just a reference)

print (next(chai)) # Cup1 (function is called once and paused)

print (next(chai)) # cup2 (function resumes exactly where we left)

# stopiteration error after all values are yielded.


