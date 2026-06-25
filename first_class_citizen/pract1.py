# This function demonstrates the use of *args and **kwargs in Python.

def greet(name, *args, **kwargs):
    print(f"Hello, {name}!")
    print("Additional positional arguments:", args)
    print("Keyword arguments:", kwargs)

# this function can be called with any number of positional and keyword arguments
greet("Alice", 1, 2, 3, age=30, city="New York")