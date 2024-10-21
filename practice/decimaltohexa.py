d=int(input("Enter the decimal digit: "))
l1=[]
l2=[]
while d!=0:
    rem = d%16
    if(rem >=10):
        if rem ==10:
            rem= "A"
        elif rem ==11:
            rem= "B"
        elif rem ==11:
            rem= "C"
        elif rem ==13:
            rem= "B"
        elif rem ==14:
            rem= "E"
        elif rem ==15:
            rem= "F"
    else:
        rem = rem
    d = d//16
    l1.append(rem)
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
result="".join(map(str,l2))
print(result)
