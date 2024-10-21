arr = [1, 5, 3, 4, 3, 5, 6]
dist_of_num={}
num=-1
for i in arr:
    dist_of_num[i]=dist_of_num.get(i,0)+1

print(dist_of_num)

for i in range(0,len(arr)):
    if dist_of_num[arr[i]]>1:
        num=i+1
        break


if num==-1:
    print(num)

else:
    print(num)