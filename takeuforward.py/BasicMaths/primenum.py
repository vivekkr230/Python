import math
n1=int(input("Enter the digit: "))
def primenumber(x):
    count=0
    for i in range(1,int(math.sqrt(x))+1):
        if x%i==0:
            count+=1
        else:
            continue
    return count

c=primenumber(n1)

if c>2:
    print(f"{n1} is not a prime number")
else:
    print(f"{n1} is a prime number")