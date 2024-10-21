b=int(input("Enter the binary number: "))
j=0
d=0
b=str(b)
for i in range(len(b)-1,-1,-1):
    digit=int(b[i])
    d=d+digit*(2**j)
    

    j=j+1
print(d)

# while b!=0:
#     rem=b%10
#     b=b//10
#     d=d+rem*(2**j)
#     print(d)
#     j=j+1



