# Pack multiple values into a tuple.
# Unpack the tuple into individual variables.
# Swap the values of two variables using tuple unpacking.

# Pack multiple values into a tuple.
details="Vivek Kumar",30,"unemployeed","software devloper"

print(details)

#other way to do it

name="vivek"
age=30
info=name,age
print(info)




# Unpack the tuple into individual variables.
food=("litti","chokha","chawal","daal","aloobhujiya")
aata,baigan,gehu,daaal,aalo=food
print(f"{aata} ,{gehu} ,{daaal}")

# Swap the values of two variables using tuple unpacking.

value1=10
value2=20
value3=40

swap=value1,value2,value3
print(swap)
value2,value1,value3=swap
print(f"after swapping :{value1},{value2},{value3}")

#more efficient way to do it
a=10
b=20
print(f"before swapping :")
print(f"a={a}")
print(f"b={b}")
a,b=b,a
print(f"after swapping:")
print(f"a={a}")
print(f"b={b}")
