l1= [-5, 7, -3, -4, 9, 10, -1, 11]

for i in range(0,len(l1)):
    x=0
    for j in range(i,0,-1):
        if l1[j]>0 and l1[j-1]<0:
            x=l1[j]
            l1[j]=l1[j-1]
            l1[j-1]=x

# for i in range(0,len(l1)-1):
#     if l1[i]<0:
#         if l1[i+1]>0:
#             x=l1[i+1]
#             l1[i+1]=l1[i]
#             l1[i]=x

#     elif l1[i]>0:
#         if l1[i-1]<0:
#             x=l1[i-1]
#             l1[i-1]=l1[i]
#             l1[i]=x

print(l1)