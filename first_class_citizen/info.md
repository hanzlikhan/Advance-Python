## first class citizen functions

- In python, functions are just another value. 
- Assign them to variable
- Pass them to other functions.
- Return them from functions
- *args = collect extrra positional arg into tuple 
- **kwargs = collect extra keyword arg into a dict. 

### *args and **kwargs (Making Functions Flexible)
Sometimes you don’t know in advance how many arguments someone will pass.

- *args → catches any extra positional arguments → stored as a tuple
- **kwargs → catches any extra keyword arguments → stored as a dictionary

### closure 

A closure is when a function remembers variables from the place where it was created, even after that outer function has finished running.