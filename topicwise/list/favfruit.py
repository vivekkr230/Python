l1=["Mango","Apple","Banana","Orange","Pineapple","Guava"]
l2=[]
# print(l1[-1])
# l1.append("Pineapple")
# print(l1)
# l1.remove("Mango")
# print(l1)
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)
# print("Apple" in l1)
print(l1[0:3])
print(l1[-3:])
print(l1)
for i in range(0,len(l1),2):
    l2.append(l1[i])
print(l2)