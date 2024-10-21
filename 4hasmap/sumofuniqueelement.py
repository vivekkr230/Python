arr=[1,2,3,2]

sum=0
dist_of_num={}

for i in arr:
    dist_of_num[i]=dist_of_num.get(i,0)+1

print(dist_of_num)

for i in arr:
    if dist_of_num[i]==1:
        sum=sum+i

print(sum)