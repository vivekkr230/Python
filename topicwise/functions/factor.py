def getfactor(x):
    for i in range(1,x+1):
        if x%i == 0 :
          l1.append(i)  
            
        else:
            continue
l1=[]
x=int(input("Enter the digit you want the factorisation"))
print("The factor of ",x,"is given below")
getfactor(x)
if(len(l1)>2):
    print("the number of factors of",x,"is",len(l1))
    print(x,"is a composite number")
else:
    print(x,"is not a composite number")