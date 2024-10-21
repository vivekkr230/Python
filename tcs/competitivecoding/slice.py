s=int(input("Enter the number of slices: "))
count=0
factor_s=[]
for i in range(1,s+1):
    if s%i == 0:
        factor_s.append(i)
    else:
        continue
print(factor_s)
while count != len(factor_s):
    