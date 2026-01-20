# Infinite generator: An infinite generator is a generator that can produce values forever (or until you stop it).
# It doesn’t store all values in memory — it generates one value at a time using yield.

def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()

for _ in range(3):
    print(next(refill)) 
# Refil #1
# Refil #2
# Refil #3

# iterates one by one but loop is not paused it prints for infinite values.