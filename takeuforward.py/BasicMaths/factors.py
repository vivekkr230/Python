import math
n1=int(input("Enter the first number: "))
def factorscalculate(x):
    l1=[]
    for i in range(1,int(math.sqrt(x)+1)):
        if x%i==0:
            l1.append(i)
            if x%i==0 and x//i != i:
                l1.append(x//i)

    l1.sort()
    return l1

print(factorscalculate(n1))
