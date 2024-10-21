def selectionsort(x):
    y=len(x)
    for j in range(0,len(x)):
        index=0
        max_num=0
        for i in range(0,y):
            if max_num < x[i]:
                max_num = x[i]
                index=i
        x[index]=x[y-1]
        x[y-1]=max_num
        y=y-1
    return x

l1=[5,9,2,11,1,7]
print(l1)
l1=selectionsort(l1)
print(l1)
