l1=[6,5,18,7,7,19,2]


def bubbleshort(l1):
    y=len(l1)
    for j in range(0,len(l1)):
        x=0
        for i in range(0,y-1-j):
            if l1[i]>l1[i+1]:
                x=l1[i+1]
                l1[i+1]=l1[i]
                l1[i]=x
        

    return l1

y=bubbleshort(l1)
print(f"After bubble sort the list is {y}")