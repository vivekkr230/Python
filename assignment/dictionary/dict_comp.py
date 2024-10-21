# Create a dictionary with numbers as keys and their squares as values using a dictionary comprehension.
# Invert the keys and values of an existing dictionary.

square_dict={x:x**2 for x in range(1,6)}
print(f"dictonary for squares : {square_dict}")


# revert the key and value
revert={value : key for key,value in square_dict.items()}
print(revert)