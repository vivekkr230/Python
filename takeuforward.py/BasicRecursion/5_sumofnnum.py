n=int(input("Enter the value of n: "))
x=0
sumof=0
def sumof1ton():
    global x,sumof
    while x<=n:
        sumof=sumof+x
        x=x+1
        sumof1ton()
    
sumof1ton()
print(sumof)