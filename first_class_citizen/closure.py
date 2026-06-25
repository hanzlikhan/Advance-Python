# This code demonstrates the concept of closures in Python. A closure is a function that retains access to variables from its enclosing scope, even after that scope has finished executing. In this example, the outer function `make_multiplier` takes a number `n` and returns an inner function `multiplier`, which multiplies its input `x` by `n`. The inner function retains access to `n`, demonstrating the closure property.

def make_multiplier(n):           # Outer function
    def multiplier(x):            # Inner function (nested)
        return x * n              # Uses 'n' from outer function
    return multiplier             # Returns the inner function

# Using the closure
# Create a function that multiplies by 3

double = make_multiplier(2)       # Create a function that multiplies by 2
print(double(5))                  # 10