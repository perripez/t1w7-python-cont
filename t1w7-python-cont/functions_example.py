def greet():
    print("I love coding!")

# Call the function
greet()

# Scope
scope_out = "outside"

def test_scope():
    print(scope_out)

test_scope()

def test_scope1():
    scope_in = "Inside"

