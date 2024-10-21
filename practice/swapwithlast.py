
l1=[4,5,6,12,10]
print(l1)
print()

x=0
index=0
for i in range(0,len(l1)):
    if x < l1[i]:
        x=l1[i]
        index=i
    else:
        x=x
# print(x)
# print(index)
l1[index]=l1[len(l1)-1]
l1[len(l1)-1]=x
# print(l1[len(l1)-1])

print()

print(l1)