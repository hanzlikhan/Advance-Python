a = [1,2,3]
b = [1,2,3]

# a and b are equal in value but not the same object in memory
if a == b:
    print("a and b are equal in value")
# a and b are not the same object in memory
if a is b:
    print("a and b are the same object in memory")

