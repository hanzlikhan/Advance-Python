# This function demonstrates the use of *args and **kwargs in Python. It takes a name as a required argument, followed by any number of additional positional arguments (*args) and keyword arguments (**kwargs). The function then prints the name, the extra positional arguments, and the extra keyword arguments.
def show_details(name, *args, **kwargs):
    print("Name:", name)
    print("Extra positional args:", args)
    print("Extra keyword args:", kwargs)

# Calling it
# The function can be called with any number of positional and keyword arguments. The first argument is the name, followed by any additional positional arguments, and then any keyword arguments.
show_details("Hanzla", 25, "Pakistan", city="Rahim Yar Khan", hobby="AI")