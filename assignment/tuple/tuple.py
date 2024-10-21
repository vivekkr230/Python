# Create a tuple with five elements and print it.
# Access and print the first and last elements of the tuple.
# Attempt to modify an element of the tuple (and observe the result).
# Convert a list into a tuple.
# Unpack the elements of a tuple into variables.
# Tuple Methods:
# Find the index of a specific element in the tuple using index().
# Count the occurrences of a specific element using count().

t1=(1,2,5,5,5,5,53,4,5,5,5,5,5)# write it with or without ""
print(t1)

print(t1[0])
print(t1[-1])

l1=[1,2,3,4,5,6]
print(tuple(l1))


print(t1.index(4))
print(t1.count(5))