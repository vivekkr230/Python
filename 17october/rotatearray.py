# l1=[]

# t=int(input("Enter the number of terms: "))

# for i in range(0,t):
#     y=int(input(f"Enter the {i}th element of list: "))
#     l1.insert(i,y)

# def rotatearray(l1):

#     rotate=int(input("Enter the number you want to rotate: "))

#     for i in range(0,rotate):
#         temp=l1[t-1]
#         for j in range(t-1,0,-1):
#             # print(j)
#             l1[j]=l1[j-1]
#         l1[0]=temp

#     return l1
        
       
# z=rotatearray(l1)

# print(f"After rotating the array is {l1}")


l1=[1,2,3,4,5]
k=int(input("Enter the no of times you want to rotate: "))

# for i in range(0,k):
#     for j in range(len(l1)-1,0,-1):
#         x=l1[j]
#         l1[j]=l1[(j+k)%(len(l1))]
#         l1[(j+k)%(len(l1))]=x


for i in range(0, len(l1)-1):
    index = (i+k)%len(l1)
    
    temp = l1[index]
    l1[index] = l1[i]
    l1[i] = temp

print(l1)