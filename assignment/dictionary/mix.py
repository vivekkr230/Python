# Create a dictionary with keys as fruit names and values as their prices.
# Access the price of a specific fruit using its key.
# Add a new fruit and its price to the dictionary.
# Update the price of an existing fruit.
# Remove a fruit from the dictionary using del.
# Get the length of the dictionary.

fruits={
    "Apple":500,
    "Banana":50,
    "Mango":180,
    "Guava":45
}
fruits["cherry"]=950
print(f"after adding : {fruits}")
del fruits["Apple"]
print(f"After deleting: {fruits}")
print(fruits)
fruits["Banana"]=900
print(f"after updating banana price :{fruits} ")