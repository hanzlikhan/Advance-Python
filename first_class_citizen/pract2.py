# This code demonstrates that functions in Python are first-class citizens, meaning they can be assigned to variables, passed as arguments, and returned from other functions.
def sayHello():
    print("Hello, World!")

sayHello()

greet = sayHello  # Assigning the function to a variable
greet()  # Calling the function using the variable