# Greeting someone
def greet():
    print("Hello Coder, Perri!")

greet()

# Generalised Coding

def greet(name): # <-- Parameter
    print(f"Hello Coder, {name}!")

greet("Perri") # <-- Arguments
greet("Liam")

# Multiple Parameters

def greetings(fname, lname): # <-- Multiple Parameters
    print(f"Hello Coder, {fname} {lname}!")

greetings("Perri", "Adkins") 

# Positional Arguments

def subtract(a, b): 
    difference = a - b
    return difference

result = subtract(10,5) # <-- Positional Arguments
print(result)

# Optional Parameter

def subtract(a, b=1): # <-- Optional Parameter (used if argument is not defined below)
    difference = a - b
    return difference

result = subtract(10) # <-- Default Arguments
print(result)

# Keyword arguments 

def subtract(a, b=1): 
    difference = a - b
    return difference

result = subtract(a=10, b=5) # <-- Keyword Arguments
print(result)



