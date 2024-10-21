# Working with Nested Tuples:
# Create a tuple of tuples (e.g., representing coordinates).
# Access elements from the nested tuples.
# Use Cases for Tuples:
# Explain when you would use a tuple instead of a list.
# Create a function that returns multiple values as a tuple.


nested_tuple=(94,54,23,56,(34,66,74),4,3,1)
print(nested_tuple[4][2])

# Explain when you would use a tuple instead of a list.
# when we want to store the related information and do not want to change it


# Create a function that returns multiple values as a tuple.

def multipletuple():
    name="raju"
    age=45
    city="udaypur"
    return name,age,city

info=multipletuple()
print(info)