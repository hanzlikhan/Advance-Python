# This code demonstrates that functions can be returned from other functions in Python, showcasing the concept of first-class citizens.
def get_greeting_function(language):
    if language == "en":
        def greet():
            print("Hello!")
        return greet                    # Returning the function itself
    
    elif language == "ur":
        def greet():
            print("Assalam o Alaikum!")
        return greet

# Get a function based on language
# The returned function can be assigned to a variable and called later.
my_greeter = get_greeting_function("ur")
my_greeter()          # Assalam o Alaikum!