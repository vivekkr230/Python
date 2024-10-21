num_list=[]
count=0
flag=True
tot_sum=0
avg=0
while flag == True:
    num=int(input("Enter the number: "))
    if(num == -1):
        flag=False
        continue
    num_list.append(num)
    count +=1

#calculating the sum

for n in num_list:
    print(n)
    tot_sum=tot_sum+n
print("the total sum is ",tot_sum)
print("the count is",count)
avg=tot_sum/count
round(avg,2)

print("the average is: ",avg)