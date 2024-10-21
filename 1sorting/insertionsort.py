l1=[4,2]


for j in range(1,len(l1)):
    x=0
    for i in range(j,0,-1):
        if l1[i] < l1[i-1]:
            x=l1[i-1]
            l1[i-1]=l1[i]
            l1[i]=x

print(l1)