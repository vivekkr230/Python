l1=[]

length=int(input("Enter the length of the list: "))

for i in range(0,length):
    x=int(input(f"Enter the {i} element of list: "))
    l1.insert(i,x)

print()
print(l1)

y=int(input(f"Enter the digit you want to search: "))
count=0
for i in range(0,length):
    if l1[i]==y:
        count+=1

print(f"the number {y} occurs {count}")