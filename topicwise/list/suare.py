l1=[x**2 for x in range(1,11)]
# for i in range(1,11):
#     if (i*i)%2 == 0:
#         l1.append(i*i)
#     else:
#         continue

l2=[i for i in l1 if i%2 ==0]

print(l1)
print(l2)

l3=[[1,2,3],[6,7,7],[34,56,764]]
l4=[x for i in l3 for x in i]
print(l4)