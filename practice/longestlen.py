string="abaabbccdef"
l1=[]
count=0
for i in string:
    if i in l1:
        # print(f"{i} already exists in {l1}")
        # print(f"if statement")
        # print()
        count=count
    else:
        # print(f"{i} does not exist in {l1}")
        # print()
        l1.append(i)
        count=count+1

print(l1)
print(count)