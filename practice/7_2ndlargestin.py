l1=[3,1,45,23,89,0]


x=l1[0]
y=l1[0]
for i in range(0,len(l1)):
    if x<l1[i]:
        x=l1[i]

for i in range(0,len(l1)):
    if y<l1[i] and l1[i]!=x:
        y=l1[i]


print(x)
print(y)