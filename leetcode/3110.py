# string="zaz"
# list1=[]
# list2=[]
# list3=[]
# sum=0
# for i in range(0,len(string)):
#     val=ord(string[i])
#     list1.append(val)

# print(list1) 
# for u in range(1,len(list1)):
#     val2=list1[u-1]-list1[u]
#     if val2<0:
#         val2=(-1)*val2
#         list2.append(val2)
#     else:
#         list2.append(val2)

# print(list2)
# for v in range(0,len(list2)):
    
#     sum=sum+list2[v]

# print(sum)


s="zaz"

sum=0
for i in range(1,len(s)):
    sum=sum + abs(ord(s[i-1])-ord(s[i]))

print(sum)