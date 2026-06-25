# This code demonstrates the concept of closures in Python. A closure is a function that retains access to variables from its enclosing scope, even after that scope has finished executing. In this example, the outer function `make_multiplier` takes a number `n` and returns an inner function `multiplier`, which multiplies its input `x` by `n`. The inner function retains access to `n`, demonstrating the closure property.

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier
# Using the closure
# Create a function that multiplies by 3
double = make_multiplier(2)
triple = make_multiplier(3)

# Call the closure functions
print(double(5))   # 10
print(triple(5))   # 15