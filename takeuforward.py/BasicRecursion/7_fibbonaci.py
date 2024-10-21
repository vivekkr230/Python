t=int(input("Enter the number of terms: "))
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
sumofnum=0
def calfibonacci(n,x1,x2):
    global sumofnum
    while n!=0:
        sumofnum=x1+x2
        print(sumofnum)
        x1=x2
        x2=sumofnum
        # print(f"the value of x2 after {n} term",x2)
        # print(f"the value of x1 after {n} term",x1)
        n=n-1
print(n1)
print(n2)
calfibonacci(t,n1,n2)

    
