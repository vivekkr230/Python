# Use the append(), extend(), and insert() methods to add elements to a list.
# Use the pop() and remove() methods to delete elements from a list.
# Find the index of a specific element in the list using index().
# Count the occurrences of a specific element using count().

l1=[1,2,3,"Vivek","Kumar"]
l1.append("suku")
print(l1)

l2=["Satyam","Aariz","Surya"]
l2.extend(["Ujjwal","Shubhankar"])
print(l2)

l2.insert(0,"friends list")
print("After insert")
print(l2)

print(l2.count("Ujjwal"))

l2.insert(3,"Ujjwal")
print(l2.count("Ujjwal"))