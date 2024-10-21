# Use the keys(), values(), and items() methods to iterate through the dictionary.
# Check if a specific key exists in the dictionary using in.
# Use the get() method to access a value with a default if the key doesn't exist.
# Remove a key-value pair using pop() and popitem().


gadget={
    "item":"iPhone",
    "price":83000,
    "ram":"4gb",
    "storage":128,
    "category":"electronics"
}
product=gadget.items()
for key,value in product:
    print(f"{key}:{value}")

for key,value in gadget.items():
    print(f"{key}:{value}")

for key in gadget.keys():
    print(key)
for value in gadget.values():
    print(value)

print(gadget.pop("price","not found"))#delete a particular element

print(gadget.popitem()) #delete the last inserted element


print(gadget.get("vivek","key not found"))# to get a particular value if not then return default value