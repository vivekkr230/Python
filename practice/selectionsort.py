l1=[5,9,2,11,1,7]
print(l1)
print()

y=len(l1)
for j in range(0,len(l1)):
    print(j)
    x=0
    index=0
    for i in range(0,y):    
        if x < l1[i]:
            x=l1[i]
            index=i

    l1[index]=l1[y-1]
    l1[y-1]=x
    #     print(f"the value of i is {i}")
    # print(l1)
    # print(f"Done with the {j} iteration")
    # print("Decrease the lenght of list by 1") 
    # print()
    y=y-1
    # print(l1)
    # print(f"this is the value of current largest {x}")
    # print(f"this is the value of current index {index}")

print()
print(l1)