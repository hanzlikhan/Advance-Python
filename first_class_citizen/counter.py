# This code demonstrates the concept of closures in Python. A closure is a function that retains access to variables from its enclosing scope, even after that scope has finished executing. In this example, the outer function `create_counter` initializes a variable `count` and returns an inner function `increment`, which increments and returns the value of `count`. The inner function retains access to `count`, demonstrating the closure property.

def create_counter():
    count = 0
    
    def increment():
        nonlocal count          # Needed because we want to change the outer variable
        count += 1
        return count
    
    return increment
# Using the closure
counter = create_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3