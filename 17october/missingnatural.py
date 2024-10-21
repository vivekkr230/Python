l1=[4,5,6,1,2]
count=0
for i in l1:
    count+=1

for i in range(0,count):
    x=0
    for j in range(i,0,-1):
        if l1[j]<l1[j-1]:
            x=l1[j-1]
            l1[j-1]=l1[j]
            l1[j]=x

print(l1)

# while y!=count:
    
#     for i in range(0,count):
#         if y==l1[i]:
#             print(f"{y} is found")
#     y=y+1

for i in range(1, len(l1)+1):
    if i != l1[i-1]:
        print(i)
        break
