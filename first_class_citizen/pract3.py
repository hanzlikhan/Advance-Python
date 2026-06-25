# this function demonstrates function pass to another function as an argument
def greet(name):
    print(f"Hello, {name}!")

# this function takes another function as an argument and calls it twice
def say_goodbye():
    print("Goodbye! ")

# this function takes another function as an argument and calls it twice
def runtwice(sayHello):
    sayHello()
    sayHello()

runtwice(say_goodbye)  # passing the function say_goodbye as an argument to runtwice
print("_________")
runtwice(greet)  # passing the function greet as an argument to runtwice