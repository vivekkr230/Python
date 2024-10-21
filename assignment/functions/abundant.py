num=int(input("Enter the number to get factorissed: "))
l1=[]

#calculating the factorisation

def factor(x):
    for i in range(1,x+1):
        if i==x:
            continue
        elif x%i==0:
            l1.append(i)
        
#calculating the sum
def sum_factor():
    s=0
    for i in l1:
        s=s+i
    if s>num:
        print(num,"is abundant number")
    else:
        print(num,"is not an abundant number")
factor(num)
sum_factor()