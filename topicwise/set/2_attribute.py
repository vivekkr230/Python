my_set={1,2,3}
# print(my_set[0]) throws an error 


my_set.add(4)

print(my_set)

# my_set.remove(5) it throws an error 

my_set.discard(5) #it does not throw an error
print(my_set)

my_set.pop() # removes any element
print(my_set)

my_set.clear()
print(my_set)