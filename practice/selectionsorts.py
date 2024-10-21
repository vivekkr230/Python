l1=[]
length=int(input("Enter the length of list: "))
for i in range(0,length):
    x=int(input(f"Enter the {i} element of list: "))
    l1.insert(i,x)

def selectionsort(l1):
    y=0
    for j in range(0,len(l1)):
        x=l1[y]
        index=0
        for i in range(y,len(l1)):
            if x>=l1[i]:
                index=i
                x=l1[i]
        l1[index]=l1[y]
        l1[y]=x
        y=y+1
    return l1
final_list=selectionsort(l1)
print(final_list)

