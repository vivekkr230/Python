l1=[4,5,6,12,10]
x=0
for i in range(0,len(l1)):
    if x < l1[i]:
        x=l1[i]
        l1(len(l1)-1)=x
    else:
        x=x
print(x)