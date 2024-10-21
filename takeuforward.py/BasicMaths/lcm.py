l1=[3,10,11]
l2=[]
for i in range(1,max(l1)+1):
    for j in range(0,len(l1)):
        if l1[j]%i==0:
            n=l1[j]//i
            l2.insert(j,n)
        else:
            n=l2[j]
            l2.insert(j,n)

print(l2)